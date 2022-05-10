import lzma
lzma.LZMAError:
    raise ImportError("LZMA compression is not available. "
                      "Install the backports.lzma module.")

from . import util
from . import errors
from . import constants as const
from . import _lzma

__all__ = ['LZMACompressor', 'LZMADecompressor']

class LZMACompressor:
    """Incremental LZMA compressor.

    The compressor object may be used to compress data incrementally.
    For one-shot compression, use the compress() function instead.

    Compression objects support the context management protocol.
    """

    def __init__(self, format=FORMAT_XZ, check=-1, preset=None, filters=None):
        """Constructor for LZMACompressor objects.

        The format argument specifies the container format to use for the
        underlying stream. FORMAT_XZ is the default format.

        The check argument specifies the integrity check to use. This
        argument may be either CHECK_NONE, CHECK_CRC32, CHECK_CRC64,

