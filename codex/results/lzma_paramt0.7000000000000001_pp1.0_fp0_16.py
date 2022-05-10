from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'Hello World'
# >>>
```

Note that the data must be decompressed with the same format as it was compressed.

The following types of data can be decompressed:

* *XZ*: A single concatenated .xz stream.
* *LZMA*: A raw LZMA stream.

## Filter API

The :class:`LZMACompressor` and :class:`LZMADecompressor` classes are easy to use but
not very flexible.  If you need more control over the compression or decompression process,
use the :class:`LZMAFile` class.

```python
import lzma
f = lzma.LZMAFile('/tmp/foo.xz')
data = f.read()
f.close()

# Or use the context manager
with lzma.LZMAFile('/tmp/foo.xz') as f:
    data = f.read()
```

The :class:`LZMAFile` class can be used to decompress data
