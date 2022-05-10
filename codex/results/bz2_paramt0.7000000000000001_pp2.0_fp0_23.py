from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(raw)

```

```
raw = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

from bz2 import BZ2Decompressor
print(BZ2Decompressor().decompress(raw))

```

```
>>> import bz2
>>> un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
>>> pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\
