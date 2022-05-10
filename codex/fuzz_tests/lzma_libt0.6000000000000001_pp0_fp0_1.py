import lzma
lzma.LZMAError

from . import _decompress
from . import _compress
from . import _check

__all__ = ['decompress', 'compress']

# Decompress an LZMA-compressed string.

def decompress(string, format=FORMAT_AUTO, memlimit=None, filters=None):
    """Decompresses a compressed string.

    The format parameter, if given, must be FORMAT_AUTO, FORMAT_XZ,
    FORMAT_ALONE, FORMAT_RAW, or FORMAT_UNKNOWN. If format is not given,
    FORMAT_AUTO is used. FORMAT_AUTO detects the format based on the magic
    header bytes of the compressed string. If there are no magic header bytes
    (that is, the input is raw compressed data), FORMAT_RAW is assumed.

    If the format is FORMAT_AUTO, FORMAT_ALONE, or FORMAT_XZ, the input must be
    the result of compressing a string with compress() or the
    compressfile() method of an LZMAComp
