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

def decompress_xz(data):
    #_lzma.LZMADecompressor()
    #return _lzma.LZMADecompressor(format=FORMAT_XZ, filters=[{"id":_lzma.FILTER_LZMA2, "preset": 9 | _lzma.PRESET_EXTREME}])
    #pyliblzma_version = _lzma. __version__.split('.')
    #if int(pyliblzma_version[0]) > 0 or int(p
