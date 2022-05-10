import bz2
bz2.BZ2File?
f = bz2.BZ2File('example.bz2')
type(f)

for line in f:
    print(line)

from bz2 import BZ2File

f = BZ2File('example.bz2')
for line in f:
    print(line)

import gzip
gzip.open?
f = gzip.open('example.gz')
for line in f:
    print(line)

from gzip import open as gopen
f = gopen('example.gz')
for line in f:
    print(line)

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)
zlib.crc32(s)

import struct
struct.pack('>i4sh', 7, b'spam', 8)
data = struct.unpack('>i4sh', b'\x00\x00\x00
