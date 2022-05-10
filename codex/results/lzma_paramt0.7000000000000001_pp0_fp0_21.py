from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzmaffi'

from lzmaffi.lzma import (
    LZMADecompressor, LZMACompressor,
    FORMAT_AUTO, FORMAT_XZ, FORMAT_ALONE, FORMAT_RAW,
    check, compress, decompress,
)
