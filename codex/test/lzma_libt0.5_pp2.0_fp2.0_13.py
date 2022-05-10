import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

# Python 2.7
try:
    import zlib
    zlib_compress = zlib.compress
    zlib_decompress = zlib.decompress
except ImportError:
    pass

# Python 3.x
try:
    import gzip
    gzip_compress = gzip.compress
    gzip_decompress = gzip.decompress
except ImportError:
    pass

# Python 3.x
try:
    import bz2
    bz2_compress = bz2.compress
    bz2_decompress = bz2.decompress
except ImportError:
    pass

# Python 3.x
try:
    import lzma
    lzma_compress = lzma.compress
    lzma_decompress = lzma.decompress
except ImportError:
    pass

# Python 3.3+
