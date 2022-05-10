from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

```

```python
# 压缩
import bz2
uncompressed_data = b'Welcome to the Psycopg2 tutorial'
compressed_data = bz2.compress(uncompressed_data)
compressed_data
# 解压
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(compressed_data)
```


## gzip


```python
# 压缩
import gzip
uncompressed_data = b'Welcome to the Psycopg2 tutorial'
with gzip.open('/tmp/uncompressed.bin', 'wb') as f:
    f.write(
