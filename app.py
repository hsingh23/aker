from flask import Flask, request, Response
from flask.ext.jsonpify import jsonify
import requests as r
from lxml import html
from iron_cache import *

cache = IronCache()
app = Flask(__name__)
s = r.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36', })
s.get("http://www.aol.com/")

def json_response(data):
    return Response(response=data, status=200, mimetype="application/json")

@app.route("/")
def default():
    return jsonify(["http://upload.wikimedia.org/wikipedia/commons/3/35/SMirC-what.svg"])


@app.route("/<query>")
def web(query):
    query = query.encode('ascii', 'ignore').lower().strip()
    if not query:
        return jsonify(["http://upload.wikimedia.org/wikipedia/commons/3/35/SMirC-what.svg"])
    try:
        cached = cache.get(cache="web", key=query).value
        if "callback" in request.args:
            return "{callback}({data});".format(callback=request.args.get("callback"), data=cached)
        else:
            return cached
    except r.HTTPError:
        data = s.get("http://search.aol.com/aol/search?q={}".format(query)).text
        links = [link.attrib["href"] for link in html.fromstring(data).find_rel_links("f:url")]
        cache.put(cache="web", key=query, value=str(links))
        return jsonify(links)

@app.route("/images/<query>")
def images(query):
    query = query.encode('ascii', 'ignore').lower().strip()
    if not query:
        return jsonify(["http://upload.wikimedia.org/wikipedia/commons/3/35/SMirC-what.svg"])
    try:
        cached = cache.get(cache="images", key=query).value
        if "callback" in request.args:
            return "{callback}({data});".format(callback=request.args.get("callback"), data=cached)
        else:
            return cached
    except r.HTTPError:
        data = s.get("http://search.aol.com/aol/image?q={}".format(query)).text
        links = [link.attrib["href"] for link in html.fromstring(data).find_rel_links("f:url")]
        cache.put(cache="images", key=query, value=str(links))
        return jsonify(links)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
