from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
b'foo and bar and qux'
```

The LZMA algorithm can also utilize a dictionary to more efficiently compress
data at the cost of increasing the size of the compressed file.

```python
from lzma import LZMADecompressor, FORMAT_AUTO

dictionary = b'some useful data that the decompressor will probably see again'

decompressor = LZMADecompressor(FORMAT_AUTO, dictionary=dictionary)
decompressor.decompress(compressed)
b'foo and bar and qux'
```

For more details, see [the documentation](https://docs.python.org/3/library/lzma.html).
