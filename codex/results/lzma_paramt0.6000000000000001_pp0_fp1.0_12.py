from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
# b'Hello World!Hello World!'
```

### Encoder
```
from lzma import LZMAEncoder
encoder = LZMAEncoder()
encoder.encode(b'Hello World!Hello World!')
# b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x01\xa8\x0b\x00\x00\x00\x00"
```

### Filter
```
from lzma import LZMAFilter
LZMAFilter(check=CHECK_CRC64, preset=9, filters=[{'id': FILTER_LZMA1, 'dict_size': 1 << 23, 'lc': 3, 'lp': 0, 'pb': 2}, {'id': FILTER_DELTA, 'dist': 1}])
# <lzma.LZ
