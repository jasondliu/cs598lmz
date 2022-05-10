from lzma import LZMADecompressor
LZMADecompressor()

from bz2 import BZ2Decompressor
BZ2Decompressor()

from zlib import Decompressobj
Decompressobj()

from zlib import decompress as zlib_decompress
zlib_decompress(b"")

from lzma import decompress as lzma_decompress
lzma_decompress(b"")

from bz2 import decompress as bz2_decompress
bz2_decompress(b"")
