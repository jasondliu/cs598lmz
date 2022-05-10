from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
```

```python
class LZMACompressor(object):
    def __init__(self, format=None, check=-1, preset=None, filters=None):
        # ...
    def compress(self, data):
        # ...
    def flush(self):
        # ...

class LZMADecompressor(object):
    def __init__(self):
        # ...
    def decompress(self, data):
        # ...

class BZ2Compressor(object):
    def __init__(self, compresslevel=9):
        # ...
    def compress(self, data):
        # ...
    def flush(self):
        # ...

class BZ2Decompressor(object):
    def __init__(self):
        # ...
    def decompress(self, data):
        # ...
```

## 2.6 通用接口
