from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read()).decode()
```

```
BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084
```

Decoding this gives us the flag


#### Flag 
###### actf{bunzip2_ftw_7r3qxvix2k}
