from bz2 import BZ2Decompressor
BZ2Decompressor()

with open('example.bz2', 'rb') as input:
    decompressor = BZ2Decompressor()
    with open('example.txt', 'wt') as output:
        for block in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

import bz2
uncompressed_data = bz2.decompress(compressed_data)

import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

import zlib
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

import binascii
binascii.crc32(s)

import struct
struct.pack('>I', 10240099)

struct.unpack('>IH', b'\
