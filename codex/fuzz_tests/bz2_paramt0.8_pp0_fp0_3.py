from bz2 import BZ2Decompressor
BZ2Decompressor

from lzma import LZMADecompressor
LZMADecompressor

from zlib import decompress as zlib_decompress
zlib_decompress

from lz4 import LZ4_blockDecompress as lz4_decompress
lz4_decompress

from . import _lzma_cffi
lzma_decompress = _lzma_cffi.lzma_decompress


COMPRESSORS = {
    'zlib': zlib_compress,
    'bz2': bz2_compress,
    'lzma': lzma_compress,
    'lz4': lz4_compress,
    'snappy': snappy_compress,
}

DECOMPRESSORS = {
    'zlib': zlib_decompress,
    'bz2': bz2_decompress,
    'lzma': lzma_decompress,
    'lz4': lz4_decompress,
   
