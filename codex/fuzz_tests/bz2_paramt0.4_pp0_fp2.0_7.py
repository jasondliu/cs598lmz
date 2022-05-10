from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b"hello world"))

import lzma
lzma.decompress(lzma.compress(b"hello world"))

import zlib
zlib.decompress(zlib.compress(b"hello world"))

import gzip
with gzip.open("somefile.gz", "rb") as f:
    f.read()

import gzip
with gzip.open("somefile.gz", "wt") as f:
    f.write("hello world")

import gzip
with gzip.open("somefile.gz", "wt") as f:
    f.write("hello world")

import gzip
with gzip.open("somefile.gz", "wt", compresslevel=5) as f:
    f.write("hello world")

import gzip
with gzip.open("somefile.gz", "wt", compresslevel=9) as f:
    f.write("hello world")

import gzip
with gzip.open("somefile.gz", "wt", compress
