import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress

def _compress_wrapper(compress, level):
    def wrapper(data):
        return compress(data, level)
    return wrapper

import bz2
bz2_compress = bz2.compress
bz2_compress1 = _compress_wrapper(bz2.compress, 1)
bz2_compress9 = _compress_wrapper(bz2.compress, 9)
bz2_decompress = bz2.decompress

# Pick the best implementation available
