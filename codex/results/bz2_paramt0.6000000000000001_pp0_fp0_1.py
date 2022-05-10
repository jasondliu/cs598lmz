from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"Hello World!"))

from zlib import decompress
decompress(zlib.compress(b"Hello World!"))
