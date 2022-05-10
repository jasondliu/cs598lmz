from bz2 import BZ2Decompressor
BZ2DecompressorInputCat = FileInputCat('/dev/stdin', BZ2Decompressor)

from gzip import GzipFile
GzipFileInputCat = FileInputCat('/dev/stdin', GzipFile, mode='rb')

from lzma import LZMADecompressor
LZMADecompressorInputCat = FileInputCat('/dev/stdin', LZMADecompressor)

from zlib import decompressobj
ZlibDecompressobjInputCat = FileInputCat('/dev/stdin',
                                         decompressobj,
                                         wbits=zlib.MAX_WBITS)

from gzip import open as GzipOpen
GzipOpenInputCat = FileInputCat('/dev/stdin', GzipOpen, mode='rb')

#-----------------------------------------------------------------------
# Random
#-----------------------------------------------------------------------

# FIXME: You should be able to use this class without the external
# dependency.
# FIXME: This class should work with a non-file-like argument.

import ctypes
import ctypes.util

libc_path = ctypes.
