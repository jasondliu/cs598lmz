import bz2
bz2_compress = bz2.compress
del bz2

import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
del lzma

import zlib
zlib_compress = zlib.compress
zlib_decompress = zlib.decompress
del zlib

# http://code.google.com/p/python-snappy/
try:
    import snappy
    snappy_compress = snappy.compress
    snappy_decompress = snappy.decompress
    del snappy
    HAS_SNAPPY = True
except ImportError:
    HAS_SNAPPY = False

# http://packages.python.org/zippylib/
try:
    import zippylib
    zippylib_compress = zippylib.compress
    zippylib_decompress = zippylib.decompress
    del zippylib
    HAS_ZIPPYLIB = True
except Import
