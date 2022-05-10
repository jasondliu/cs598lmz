import lzma
lzma.LZMAError:
    raise ImportError('lzma module is not available')

from . import _lzma

from ._lzma import *
from ._lzma import _encode_filter_properties

__all__ = _lzma.__all__

#
# XZ-compressed files
#

class LZMAFile:
    """LZMAFile(filename=None, mode="r", *, format=FORMAT_AUTO, check=-1,
               preset=None, filters=None)

    Open an LZMA-compressed file in binary mode.

    filename can be either an actual file name (given as a str or bytes
    object), in which case the named file is opened, or it can be an
    existing file object to read from or write to.

    mode can be "r" for reading (default), "w" for (over)writing, "a" for
    appending, or "x" for exclusive creation. These can equivalently be
    given as "rb", "wb", "ab", and "xb" respectively.

   
