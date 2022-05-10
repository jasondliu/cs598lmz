import lzma
lzma.LZMAError:
    pass

try:
    import bz2
    bz2.BZ2Compressor
except ImportError:
    bz2 = None

try:
    import zlib
    zlib.compressobj
except ImportError:
    zlib = None

try:
    import gzip
    gzip.GzipFile
except ImportError:
    gzip = None

try:
    import lzma
    lzma.LZMACompressor
except ImportError:
    lzma = None

try:
    import lz4.frame
    lz4.frame.compress
except ImportError:
    lz4 = None

try:
    import snappy
    snappy.compress
except ImportError:
    snappy = None

try:
    import zstd
    zstd.ZstdCompressor
except ImportError:
    zstd = None

try:
    import brotli
    brotli.compress
except ImportError:
    brotli = None

try
