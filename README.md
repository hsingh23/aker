aker
====

Google search and image api
Turns out aol is easy to scrape and basically gives you google results for search. So there you go. Don't abuse this api, chances are it will be taken down. I merely made this for a proof of concept and hold no liability what so ever.

Web results:
http://aker.herokuapp.com/potato?callback=yo
```js
yo(['http://en.wikipedia.org/wiki/Potato', 'http://www.potatogoodness.com/', 'http://www.whfoods.com/genpage.php?tname=foodspice&dbid=48', 'http://www.idahopotato.com/', 'http://www.food.com/library/potato-106', 'http://nationalpotatocouncil.org/', 'http://www.bbcgoodfood.com/glossary/potato', 'http://www.uspotatoes.com/', 'http://urbanext.illinois.edu/veggies/potato.cfm', 'http://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2770/2']);
```
http://aker.herokuapp.com/potato
```json
['http://en.wikipedia.org/wiki/Potato', 'http://www.potatogoodness.com/', 'http://www.whfoods.com/genpage.php?tname=foodspice&dbid=48', 'http://www.idahopotato.com/', 'http://www.food.com/library/potato-106', 'http://nationalpotatocouncil.org/', 'http://www.bbcgoodfood.com/glossary/potato', 'http://www.uspotatoes.com/', 'http://urbanext.illinois.edu/veggies/potato.cfm', 'http://nutritiondata.self.com/facts/vegetables-and-vegetable-products/2770/2']
```

Image results:
http://aker.herokuapp.com/i/potato?callback=yo


```js
yo(['http://barringtonstageco.org/media/potato.jpg', 'http://www.newhealthguide.org/images/10434779/image001.jpg', 'http://www.potatoes.com/files/5713/4202/4172/07.jpg', 'http://oregonrural.org/wp-content/uploads/2010/10/Potato.jpeg', 'http://www.permaculture.co.uk/sites/default/files/images/greek-potato.standard%20460x345.gif', 'http://www.async.caltech.edu/~mika/potato/POTATO.jpg', 'http://www.thekitchenhotline.com/wp-content/uploads/2010/07/potatoes.jpg', 'http://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg', 'http://imgsrv.gardening.ktsa.com/image/ktsag/UserFiles/Image/P_Images/potato.jpg', 'http://static.ddmcdn.com/gif/potatoes-1.jpg', 'http://stormtubers.weebly.com/uploads/2/4/9/1/24912084/s288114508727664819_p1_i1_w1514.jpeg', 'http://upload.wikimedia.org/wikipedia/commons/3/38/5aday_sweet_potato.jpg', 'http://pngimg.com/upload/potato_png2391.png', 'http://www.europotato.org/frontpage_images/pic6.jpg', 'https://s3.amazonaws.com/suite101.com.prod/article_images/large/1030071_com_potato.jpg', 'http://static.tumblr.com/4f4c4d16d483a9db26dd3617ac92601b/c3ujeqe/mk7myuhwp/tumblr_static_istock-potato.jpg', 'http://upload.wikimedia.org/wikipedia/commons/4/47/Russet_potato_cultivar_with_sprouts.jpg', 'http://800medigap.com/wp-content/uploads/2013/09/Russett-PotatoesC.jpg', 'http://aka.weightwatchers.com/images/1033/dynamic/GCMSImages/Potato_main.jpg', 'http://upload.wikimedia.org/wikipedia/commons/0/02/Potato_with_sprouts.jpg']);
```



Todo: 
1. Make the cache expire (probably 1 week)
2. Add more details to images - like thumbnails, and image sizes
3. Add force no cache feature

Potential things I (or you) can add for images

```html
<p class="acc" property="f:title">moments from the war and</p>
<p class="acc" property="f:durl">www.cnn.com</p>
<p class="acc" property="f:url">http://i2.cdn.turner.com/cnn/dam/assets/130314204911-01-iraq-war-horizontal-large-gallery.jpg</p>
<p class="acc" property="f:thumbnail">http://t1.gstatic.com/images?q=tbn:ANd9GcSlqmtxijhfd5jAORGmKjHtuo3njhy_u6Epvl9E7qMz60r2ZvQjdx2x61K6:i2.cdn.turner.com/cnn/dam/assets/130314204911-01-iraq-war-horizontal-large-gallery.jpg</p>
<p class="acc" property="f:width">980</p>
<p class="acc" property="f:height">552</p>
<p class="acc" property="f:twidth">181</p>
<p class="acc" property="f:theight">101</p>
<p class="acc" property="f:site"></p>
<p class="acc" property="f:host">http://www.cnn.com/2013/03/15/world/gallery/iraq-war/</p>
<p class="acc" property="f:imgSize">269699</p>
<p class="acc" property="f:hostName">www.cnn.com</p>
```
