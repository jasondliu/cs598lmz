from lzma import LZMADecompressor
LZMADecompressor().decompress(data_compressed)

# This code will only make it to here if the decompress call succeeded.
# If it failed, a DecompressionError is raised, and the other block is
# executed.
```

```python
try:
    # Try to read compressed data in one step
    LZMADecompressor().decompress(data_compressed)
except LZMAError:
    # Above code failed, get the array it needed in smaller chunks
    data_compressed_chunks = array_split(data_compressed, 100)
    data_uncompressed = []
    decompressor = LZMADecompressor()
    for chunk in data_compressed_chunks:
        data_uncompressed.append(decompressor.decompress(chunk))
    data_uncompressed = b''.join(data_uncompressed)
```

# Compressors

## Legacy multithreaded compression

This API enables decompressing only. This API was added in Python 3.3.

Example:
```python
from
