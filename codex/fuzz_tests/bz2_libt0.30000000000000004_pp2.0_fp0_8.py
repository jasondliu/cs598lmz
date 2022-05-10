import bz2
bz2.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# lzma
import lzma
lzma.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# snappy
import snappy
snappy.decompress(data)
```

### Compress

```python
import bz2
bz2.compress(data)

# gzip
import gzip
gzip.compress(data)

# lzma
import lzma
lzma.compress(data)

# zlib
import zlib
zlib.compress(data)

# snappy
import snappy
snappy.compress(data)
```

### Compress and Decompress

```python
import bz2
bz2.decompress(bz2.compress(data))

# gzip
import gzip
gzip.decompress(gzip.compress(data))

