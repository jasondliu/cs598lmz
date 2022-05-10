from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

from zlib import decompress
decompress(compressed_data)

import gzip
with gzip.open('somefile.gz', 'rb') as f:
    file_content = f.read()

import bz2
with bz2.open('somefile.bz2', 'rb') as f:
    file_content = f.read()

with lzma.open('somefile.xz', 'rb') as f:
    file_content = f.read()

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

import binascii
binascii.crc32(s)

import zlib

data = b'witch which has which witches
