from lzma import LZMADecompressor
LZMADecompressor.__init__ = magic_init
from lzma import compress, decompress
from lzma import is_check_supported, FORMAT_AUTO, FORMAT_XZ
from lzma import CHECK_NONE, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256
from lzma import FILTER_DELTA, FILTER_LZMA2


class myLZMADecompressor(LZMADecompressor):
    """
    Changed to remove 'max_length' kwargs, which we don't need for the small
    files we are decompressing
    """
    def __init__(self, format=FORMAT_AUTO, memlimit=None, filters=None):
        LZMADecompressor.__init__(self, format, memlimit, filters)


LZMADecompressor = myLZMADecompressor


LZMACompressor = lzma.LZMACompressor


def lzma_decompress(data):
    """Decompress the given bytes using lz
