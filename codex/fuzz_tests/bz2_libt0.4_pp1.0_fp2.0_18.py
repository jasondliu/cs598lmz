import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

try:
    import lzma
    lzma_compress = lzma.compress
    lzma_decompress = lzma.decompress
except ImportError:
    lzma_compress = lzma_decompress = None

try:
    import snappy
    snappy_compress = snappy.compress
    snappy_decompress = snappy.decompress
except ImportError:
    snappy_compress = snappy_decompress = None

try:
    import lz4
    lz4_compress = lz4.compress
    lz4_decompress = lz4.decompress
except ImportError:
    lz4_compress = lz4_decompress = None

try:
    import brotli
