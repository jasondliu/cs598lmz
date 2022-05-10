import mmap
import os
import sys
import time
import warnings
import zlib

from . import _compat
from . import _util
from . import _winreg

__all__ = [
    'BZ2File',
    'GzipFile',
    'open',
    'compress',
    'decompress',
]

DEFLATED = 8
MAX_WBITS = zlib.MAX_WBITS

# The filename argument to GzipFile (and perhaps BZ2File) is not
# actually used for opening the named file; instead, it is used as the
# prefix of the filename inside the compressed file.  This is because
# the compressed file contains not only the compressed data, but also
# a table of contents, and possibly other metadata.  In order to
# support random-access reading of a compressed file, the compressed
# data must be stored as a series of independently compressed members.
# Each member has its own CRC and uncompressed size, and the file
# overall has its own CRC and uncompressed size.  The compressed data
# of each member is preceded by a header created by
