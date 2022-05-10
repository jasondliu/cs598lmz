from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

The `LZMADecompressor` class also supports the context management protocol,
allowing the decompressor to be used in a `with` statement.

```python
from lzma import LZMADecompressor
with LZMADecompressor() as decompressor:
    decompressor.decompress(data)
```

The decompressor object can be used to decompress data sequentially. For example,
to decompress a file that has been split into parts:

```python
from lzma import LZMADecompressor

with open('python.xz', 'rb') as inp, open('python.tar', 'wb') as out:
    decompressor = LZMADecompressor()
    for buf in iter(lambda: inp.read(1024 * 1024), b''):
        out.write(decompressor.decompress(buf))
    out.write(decompressor.flush())
```

The `LZMADecompressor` class supports two additional methods: `un
