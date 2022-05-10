import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

# 'identity' is a reserved name in Python 3.7
# https://github.com/python/cpython/blob/master/Lib/importlib/abc.py
# https://github.com/python/cpython/blob/master/Lib/importlib/_bootstrap.py
identity_compress = lambda x: x
identity_decompress = identity_compress


def compress_lzma(data, level=9):
    """Compress data with lzma."""
    return lzma_compress(data, level)


def compress_bz2(data, level=9):
    """Compress data with bz2."""
    return bz2_compress(data, level)


