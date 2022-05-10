import lzma
lzma.open(file_name, mode='rt')

# gzip
import gzip
gzip.open(file_name, mode='rt')

# bz2
import bz2
bz2.open(file_name, mode='rt')

# lz4
import lz4.frame
lz4.frame.open(file_name, mode='rt')

# brotli
import brotli
brotli.open(file_name, mode='rt')

# zstandard
import zstandard
zstandard.open(file_name, mode='rt')
```

## Compression

```python
# lzma
import lzma
lzma.open(file_name, mode='wt')

# gzip
import gzip
gzip.open(file_name, mode='wt')

# bz2
import bz2
bz2.open(file_name, mode='wt')

# lz4
import lz4.frame
lz4.frame.open(file_name, mode='
