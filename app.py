from flask import Flask, request
from flask.ext.jsonpify import jsonify
import requests as r
from lxml import html
from iron_cache import *

cache = IronCache()
app = Flask(__name__)
s = r.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36', })
s.get("http://www.aol.com/")
@app.route("/<query>")
def hello(query):
    query = query.encode('ascii', 'ignore').lower().strip()
    cached = cache.get(cache="links", key=query)
    if cached:
        return jsonify(cached)
    else:
        data = s.get("http://search.aol.com/aol/search?q={}".format(query)).text
        links = [link.attrib["href"] for link in html.fromstring(data).find_rel_links("f:url")]
        cache.put(cache="links", key=query, value=str(links))
    return jsonify(links)

if __name__ == "__main__":
    app.run(debug=True)
