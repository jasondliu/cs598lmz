import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

try:
    import lzma
except ImportError:
    from backports import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

try:
    import snappy
except ImportError:
    snappy = None

try:
    import zstandard as zstd
except ImportError:
    zstd = None

from . import compression

from .compression import (
    zlib_compress, zlib_decompress,
    blosc_compress, blosc_decompress,
    blosc_compress_to_buffer, blosc_decompress_from_buffer,
)

from .compression import (
    snappy_compress, snappy_decompress,
    lz4_compress, lz4_decompress,
    lz4hc_compress, lz4hc_decompress,
   
