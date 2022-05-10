import lzma
lzma.LZMACompressor()
lzma.LZMADecompressor()

import bz2
bz2.BZ2Compressor()
bz2.BZ2Decompressor()

import zlib
zlib.compress(b"Hello, world!")
zlib.decompress(b"x\x9cK\xcb\xcf\x07\r\x00\x02\x82P\xfd\x85\x88\x0b\x1a\x8a\x8b\x04\x00\x00\x00")

import gzip
gzip.compress(b"Hello, world!")
gzip.decompress(b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\xcbH\xcd\xc9\xc9W\x08\xcf/\xcaI\x01\x00\x1b\x8a\x04\x8a\x05\
