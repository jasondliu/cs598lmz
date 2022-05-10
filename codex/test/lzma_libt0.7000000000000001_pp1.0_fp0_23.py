import lzma
lzma.compress(b"Hello, world!")

import bz2
bz2.compress(b"Hello, world!")

import zlib
zlib.compress(b"Hello, world!")

import gzip
gzip.compress(b"Hello, world!")
# gzip.open() will open a compressed file and return a file-like object
import gzip

