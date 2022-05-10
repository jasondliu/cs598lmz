import bz2
bz2.decompress(b)
#bz2.decompress(b).decode("utf-8")

import gzip
#gzip.decompress(g).decode("utf-8")
gzip.decompress(g)

import lzma
lzma.decompress(x).decode("utf-8")

import zlib
zlib.decompress(z).decode("utf-8")
