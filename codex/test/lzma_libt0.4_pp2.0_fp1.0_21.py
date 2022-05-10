import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import gzip
gzip.decompress(gzip.compress(b'Hello World'))

import zipfile
