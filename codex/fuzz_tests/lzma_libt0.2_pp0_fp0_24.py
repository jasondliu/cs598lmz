import lzma
lzma.LZMA_AVAILABLE = True
except ImportError:
    lzma = None

try:
    import bz2
except ImportError:
    bz2 = None

try:
    import zlib
except ImportError:
    zlib = None

try:
    import gzip
except ImportError:
    gzip = None

try:
    import lz4.frame
    lz4.LZ4_AVAILABLE = True
except ImportError:
    lz4 = None

try:
    import snappy
    snappy.SNAPPY_AVAILABLE = True
except ImportError:
    snappy = None

try:
    import brotli
    brotli.BROTLI_AVAILABLE = True
except ImportError:
    brotli = None

try:
    import zstandard as zstd
    zstd.ZSTD_AVAILABLE = True
except ImportError:
    zstd = None

try:
    import lzf
    lzf.LZF
