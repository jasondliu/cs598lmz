from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bzip2
import bz2
bz2.decompress(data)

# gzip
import gzip
gzip.decompress(data)

# zlib
import zlib
zlib.decompress(data)

# brotli
import brotli
brotli.decompress(data)

# snappy
import snappy
snappy.decompress(data)

# lzf
import lzf
lzf.decompress(data)

# lz4
import lz4
lz4.decompress(data)

# zstd
import zstd
zstd.decompress(data)

# blosc
import blosc
blosc.decompress(data)
```

## Supported Python Versions

Python 2.7, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9

## License

This library is licensed under the MIT License.
