from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bz2
import bz2
bz2.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# lz4
import lz4.block
lz4.block.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# snappy
import snappy
snappy.uncompress(data)

# zstd
import zstandard
zstandard.ZstdDecompressor().decompress(data)
```

## Compression

```python
# lzma
import lzma
lzma.compress(data)

# bz2
import bz2
bz2.compress(data)

# zlib
import zlib
zlib.compress(data)

# gzip
import gzip
gzip.compress(data)

# lz4

