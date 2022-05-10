import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    import zlib
    zlib_compress = zlib.compress
    zlib_decompress = zlib.decompress
except ImportError:
    zlib_compress = None
    zlib_decompress = None

try:
    import bz2
    bz2_compress = bz2.compress
    bz2_decompress = bz2.decompress
except ImportError:
    bz2_compress = None
    bz2_decompress = None

try:
    import lz4.frame
    lz4_compress = lz4.frame.compress
    lz4_decompress = lz4.frame.decompress
except ImportError:
    lz4_compress = None
    lz4_decompress = None

