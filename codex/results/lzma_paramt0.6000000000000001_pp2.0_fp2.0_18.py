from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_RAW, filters=[{"id": LZMA_FILTER_LZMA2, "preset": 9 | LZMA_PRESET_EXTREME}])
```

### LZMA2 (xz)

```python
from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ)
```

### LZMA2 (xz, extreme preset)

```python
from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ, preset=9 | LZMA_PRESET_EXTREME)
```

### LZMA2 (xz, extreme filter)

```python
from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ, filters=[{"id": LZMA_FILTER_LZMA2, "preset": 9 | LZMA_PRESET_EXTREME}])
```

## Compression


