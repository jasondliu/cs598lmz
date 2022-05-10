from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"Hello World!"))

import zlib
zlib.compress(b"Hello World!")
zlib.decompress(zlib.compress(b"Hello World!"))

print(zlib.crc32(b"Hello World!"))

import sys
sys.getsizeof(b"Hello World!")

import os
os.path.getsize("/usr/share/dict/words")

import gzip
f = gzip.open("/usr/share/dict/words.gz")
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f.read(10)
f
