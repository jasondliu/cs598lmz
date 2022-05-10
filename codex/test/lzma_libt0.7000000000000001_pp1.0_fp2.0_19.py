import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    from zlib import compress as zlib_compress
    from zlib import decompress as zlib_decompress
    zlib_available = True
except ImportError:
    zlib_available = False

