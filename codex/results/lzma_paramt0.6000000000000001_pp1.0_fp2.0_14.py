from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# the data is compressed with the lz4, lz4hc, or lz4frame algorithms
from lz4 import LZ4Decompressor
LZ4Decompressor().decompress(data)

# the data is compressed with the zstd algorithm
from zstandard import ZstdDecompressor
ZstdDecompressor().decompress(data)
```

### Compression

```python
from compress import Compressor

# compress some data
compressor = Compressor()
data = b"Hello, World!"
compressed = compressor.compress(data)

# decompress the data
decompressed = compressor.decompress(compressed)

# check the data integrity
assert data == decompressed
```

### Decompression

```python
from compress import Decompressor

# decompress some data
decompressor = Decompressor()
data = b"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
