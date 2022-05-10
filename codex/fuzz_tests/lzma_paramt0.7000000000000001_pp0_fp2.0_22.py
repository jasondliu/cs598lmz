from lzma import LZMADecompressor
LZMADecompressor.decompress(<compressed data>)
```

To decompress multiple compressed blocks, you can pass the data to the `decompress` method in chunks, and it will return the decompressed data so far:

```python
from lzma import LZMADecompressor
d = LZMADecompressor()
decompressed_data = d.decompress(compressed_data_part1)
decompressed_data += d.decompress(compressed_data_part2)
...
decompressed_data += d.decompress(compressed_data_partN)
```

It is also possible to use a `LZMADecompressor` object as a context manager:

```python
from lzma import LZMADecompressor
compressed_data = ...
with LZMADecompressor() as d:
    decompressed_data = d.decompress(compressed_data)
```

In this case, the `LZMADecompressor` object will be reset after the `with` block,
