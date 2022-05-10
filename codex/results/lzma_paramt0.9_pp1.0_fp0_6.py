from lzma import LZMADecompressor
LZMADecompressor()
```

```python
from lzma import LZMACompressor
LZMACompressor(format=FORMAT_ALONE, check=-1, preset=None, filters=None)
compressor.compress(data)
compressor.flush()
compressor.get_setting()
compressor.set_setting(compress_setting)
```

```python
from lzma import LZMADecompressor
LZMADecompressor(format=None, filters=None)
decompressor.decompress(data)
decompressor.flush()
```

```python
from lzma import check_is_supported, FILTER_LZMA1, FILTER_LZMA2
check_is_supported(check)
check_is_supported(None, filters=[FILTER_LZMA1, FILTER_LZMA2])
```
