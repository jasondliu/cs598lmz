from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

LZMADecompressor().decompress(data, max_length=4)

from lzma import open
f = open(filename, "rt")
f.read()
f.close()

import bz2

from bz2 import BZ2Compressor, BZ2Decompressor
compressor = BZ2Compressor()
compressor.compress(data)

decompressor = BZ2Decompressor()
decompressor.decompress(data)

from bz2 import open
f = open(filename, "rt", encoding="utf-8")
f.read()
f.close()

import zlib

from zlib import compress, decompress
compress(data)

decompress(data)

import zlib
zlib.compress(data)

zlib.decompress(data)

import zlib
compressobj = zlib.compressobj()
compressobj.compress(data1)
compressobj.compress(data2)
compressobj
