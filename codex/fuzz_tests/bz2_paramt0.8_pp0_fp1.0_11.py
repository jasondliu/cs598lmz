from bz2 import BZ2Decompressor
BZ2Decompressor()
```

```
import bz2
input = b'Hello'
compressed = bz2.compress(input)
compressed
b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
```

```
len(compressed)
37
len(input)
5
```

```
bz2.decompress(compressed)
b'Hello'
```

#### Compressing and decompressing data

```
import bz2
uncompressed_data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
