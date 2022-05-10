from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# The decompressor object can also be used as a context manager
# (see section Using Context Managers of the Python Language Reference):
with LZMADecompressor() as decompressor:
    decompressor.decompress(data)
```

`LZMACompressor` and `LZMADecompressor` support the context management protocol.

```python
import lzma

with lzma.open('foo.xz', 'w') as f:
    f.write(b'hello world')
```

`lzma.open` accepts the same arguments as the built-in `open`, except that `encoding` and `newline` are not supported.

The `lzma` module supports the following compression filters:

* `LZMA_FILTER_LZMA1`
* `LZMA_FILTER_LZMA2`
* `LZMA_FILTER_DELTA`
* `LZMA_FILTER_X86`
* `LZMA_FILTER_IA64`
