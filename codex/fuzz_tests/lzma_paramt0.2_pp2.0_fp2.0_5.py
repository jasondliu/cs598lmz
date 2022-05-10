from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'
```

## LZMAFile

The `LZMAFile` class provides a file-like interface to LZMA-compressed files.

```python
from lzma import LZMAFile
with LZMAFile('lzma_file.xz', 'w') as f:
    f.write(b'hello world')

with LZMAFile('lzma_file.xz', 'r') as f:
    print(f.read())

# Output: b'hello world'
```

## LZMACompressor and LZMADecompressor

The `LZMACompressor` and `LZMADecompressor` classes provide a simple interface
to compress and decompress data streams.


