from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZ").decode("ascii")
BZ2Decompressor().decompress(b"BZh9").decode("ascii")
