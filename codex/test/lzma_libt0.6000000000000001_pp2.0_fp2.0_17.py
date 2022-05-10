import lzma
lzma.LZMAError

try:
    import bz2
    bz2.BZ2Compressor
except ImportError:
    bz2 = None

import zlib
zlib.MAX_WBITS

try:
    import zstd
    zstd.ZstdDecompressor
except ImportError:
    zstd = None

try:
    import brotli
    brotli.BrotliDecompressor
except ImportError:
    brotli = None

import base64
