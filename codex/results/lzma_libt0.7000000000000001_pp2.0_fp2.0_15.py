import lzma
lzma_compress = lzma.compress

def lzma_decompress(data):
    return lzma.decompress(data, format=lzma.FORMAT_RAW)

try:
    from zlib import compress as zlib_compress, decompress as zlib_decompress
except ImportError:
    zlib_compress = zlib_decompress = None

try:
    import bz2
    bz2_compress = bz2.compress
    bz2_decompress = bz2.decompress
except ImportError:
    bz2_compress = bz2_decompress = None

try:
    from snappy import compress as snappy_compress, decompress as snappy_decompress
except ImportError:
    snappy_compress = snappy_decompress = None

try:
    from lz4 import compress as lz4_compress, decompress as lz4_decompress
except ImportError:
    lz4_compress = lz
