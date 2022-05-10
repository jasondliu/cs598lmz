from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(res.content)

```

```
b'BZh91AY&SYA\xc4\x82:\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
```
![image.png](attachment:image.png)

## Step 3: Find the page behind the URL

The same page is behind each of the following URLs:

```
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682
```

Each page simply tells you to visit the next one. The goal is to keep on following these links until you find the page that tells you to visit another URL.

## Step 4: Follow the chain of links


