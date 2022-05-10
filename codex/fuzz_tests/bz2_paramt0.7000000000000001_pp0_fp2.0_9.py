from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(c_compressed)

import bz2
bz2.decompress(c_compressed)

# gzip decompression
import gzip
gzip.decompress(g_compressed)

# zlib decompression
import zlib
zlib.decompress(z_compressed)

```

### Compressing files

```python

# bz2 compression
import bz2
bz2_compressor = bz2.BZ2Compressor()
result = b''
for block in blocks:
    result += bz2_compressor.compress(block)
result += bz2_compressor.flush()

with open('somefile.bz2', 'wb') as f:
    f.write(result)

# gzip compression
import gzip

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# gzip compression with a custom compress level
import gzip

with gzip.open('somefile.gz', 'wt',
