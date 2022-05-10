from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('myfile.bz2', 'rb').read())
```

### LZMA

```python
from lzma import LZMADecompressor
LZMADecompressor().decompress(open('myfile.xz', 'rb').read())
```

### LZ4

```python
from lz4 import decompress
decompress(open('myfile.lz4', 'rb').read())
```

### Snappy

```python
from snappy import decompress
decompress(open('myfile.snappy', 'rb').read())
```

### LZ77

```python
from lz77 import decompress
decompress(open('myfile.lz77', 'rb').read())
```


### Fuzzy

```python
from fuzzy import decompress
decompress(open('myfile.fuzzy', 'rb').read())
```

### Zstandard

```python
from zstandard import ZstdDecompressor
Z
