from bz2 import BZ2Decompressor
BZ2Decompressor()
print("done")

from lzma import LZMADecompressor
LZMADecompressor()
print("done")

import zlib
zlib.compressobj()
zlib.decompressobj()
print("done")

import _lzma
_lzma.LZMADecompressor()
