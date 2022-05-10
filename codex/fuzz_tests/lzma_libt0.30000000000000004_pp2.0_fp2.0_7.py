import lzma
lzma.LZMAError:
    pass

from . import _lzma

#
# Exceptions
#

class Error(Exception):
    """Base class for errors in the lzma module."""
    pass

class LZMAError(Error):
    """Exception raised for errors that are related to the LZMA
    compression or decompression.
    """
    pass

#
# Constants from the C header
#

FILTER_LZMA1 = _lzma.FILTER_LZMA1
FILTER_LZMA2 = _lzma.FILTER_LZMA2

FORMAT_AUTO = _lzma.FORMAT_AUTO
FORMAT_XZ = _lzma.FORMAT_XZ
FORMAT_ALONE = _lzma.FORMAT_ALONE
FORMAT_RAW = _lzma.FORMAT_RAW

MODE_FAST = _lzma.MODE_FAST
MODE_NORMAL = _lzma.MODE_NORMAL

PRESET_DEFAULT = _l
