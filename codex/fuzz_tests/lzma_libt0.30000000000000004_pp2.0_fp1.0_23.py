import lzma
lzma.LZMAError:
    print("LZMA compression is not available")
    lzma = None

try:
    import bz2
except ImportError:
    print("BZ2 compression is not available")
    bz2 = None

try:
    import zlib
except ImportError:
    print("ZLIB compression is not available")
    zlib = None

try:
    import lz4
except ImportError:
    print("LZ4 compression is not available")
    lz4 = None

try:
    import snappy
except ImportError:
    print("Snappy compression is not available")
    snappy = None

try:
    import brotli
except ImportError:
    print("Brotli compression is not available")
    brotli = None

try:
    import zstd
except ImportError:
    print("ZSTD compression is not available")
    zstd = None

try:
    import blosc
except ImportError:
    print("Blosc compression is not available")
    blosc = None

try
