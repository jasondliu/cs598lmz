import lzma
lzma.LZMAError.__module__ = "lzma"

from .._compat import text_type, binary_type, implements_to_string

from ..exceptions import LZMAError
from .common import Compressor, Decompressor, BufferFull, BUFFER_SIZE, OPEN_READ_BUFFER_SIZE, OPEN_WRITE_BUFFER_SIZE, \
    OPEN_READ_BUFFER_SIZE, OPEN_WRITE_BUFFER_SIZE


__all__ = ["LZMACompressor", "LZMADecompressor"]


class LZMACompressor(Compressor):
    """
    LZMA Compressor.

    Compresses data incrementally.

    The compressor object may not be used after the close() method has been
    called.

    Attributes:

    * preset: Compression preset. The preset must be an integer in the range
      0-9, inclusive, or a preset supported by the backend. The default value
      is 6.

    * format: Compression format. The format must be one of the following
      constants: FORMAT_XZ, FOR
