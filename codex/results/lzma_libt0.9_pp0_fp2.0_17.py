import lzma
lzma.register_lzma_options(lzmamodule)
import StringIO

__all__ = [
    "decompress",
    "compress",
    "BZ2Compressor",
    "BZ2Decompressor",
]

MARK_END = '\x00'

def compress(data, option=None):
    """compress input data

    Args:
        data (string): input data
        option (dict): option for compress
            {
                filter: liblzma.FILTER_LZMA2,
                preset: 9,
                lc: liblzma.LZMA_LC_CTYPE,
                lp: liblzma.LZMA_LP_DEFAULT,
                pb: liblzma.LZMA_PB_DEFAULT,
            }

    Return:
        string: compressed data

    Raise:
        ValueError: if input data and output data are not a BufferType
    """
    if type(data) != str and not isinstance(data, BufferType):
       
