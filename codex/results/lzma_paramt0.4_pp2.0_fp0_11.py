from lzma import LZMADecompressor
LZMADecompressor()

import zlib
zlib.decompressobj()

from zlib import decompress
decompress(b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x1a\x8b\x08\x00')

import bz2
bz2.BZ2Decompressor()

from bz2 import BZ2Decompressor
BZ2Decompressor()

from bz2 import decompress
decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

import lz4.frame
lz4.frame.decompress(b'\xf3H\xd2\x01\x0b\x00\x10\x00\x00\x00\x00')

