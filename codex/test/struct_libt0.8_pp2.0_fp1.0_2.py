import _struct
import _lzma
import zlib

CHUNK = 16 * 1024

def decompress(compressed):
    """zlib.decompressobj(wbits=-zlib.MAX_WBITS)
    Return a decompressor object.
    For more information see:
    http://docs.python.org/2/library/zlib.html#zlib.decompressobj
    """
    return zlib.decompressobj(wbits=-zlib.MAX_WBITS)

