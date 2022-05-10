from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# <LZMAFilePaths: src='<fdopen>', dest='<fdopen>'>
# b'Hello Python World!'
```

### Compress data

```python
from lzma import LZMACompressor
data = LZMACompressor().compress(b'Hello Python World!')
data

# b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'
```

### Compress data to file

```python
from lzma import LZMACompressor

with open('test.xz', 'wb') as fd
