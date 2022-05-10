from bz2 import BZ2Decompressor
BZ2Decompressor.__doc__ = """\
A decompressor object for the bzip2 compression format.

The decompressor object may be used to decompress data incrementally.

For one-shot decompression, use the decompress() function instead.

Methods:

decompress(data) -- Return decompressed string.

Attributes:

unused_data -- Bytes that were not decompressed (read-only).
"""

from lzma import LZMADecompressor
LZMADecompressor.__doc__ = """\
A decompressor object for the XZ compression format.

The decompressor object may be used to decompress data incrementally.

For one-shot decompression, use the decompress() function instead.

Methods:

decompress(data) -- Return decompressed string.

Attributes:

unused_data -- Bytes that were not decompressed (read-only).
"""

from zlib import decompress, decompressobj, MAX_WBITS, Z_DEFAULT_COMPRESSION, Z_FILTERED, Z_FINISH, Z_FULL
