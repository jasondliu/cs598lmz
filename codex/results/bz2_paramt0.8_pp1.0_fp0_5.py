from bz2 import BZ2Decompressor
BZ2Decompressor().flush() == b''

from zlib import ZlibCompressobj
ZlibCompressobj().flush() == b''
