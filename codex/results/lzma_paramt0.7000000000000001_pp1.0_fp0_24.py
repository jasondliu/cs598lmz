from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_file)
# ... or in one line, with an explicit LZMA file header:
LZMADecompressor(lzma.FORMAT_RAW).decompress(lzma_file)
```

The LZMA format supports special options that can be set when compressing to
control the compression level and other parameters. These can be specified
when constructing the LZMADecompressor object:

```python
from lzma import LZMADecompressor
from lzma import FORMAT_RAW, FILTER_LZMA1, CHECK_CRC32
decompressor = LZMADecompressor(FORMAT_RAW, filters=[
    {"id": FILTER_LZMA1, "dict_size": 4400000, "lc": 3, "lp": 0, "pb": 2, "mode": 0, "nice_len": 128, "mf": 0, "depth": 0},
    {"id": CHECK_CRC32},
])
decompressor.decompress(lzma_file)
``
