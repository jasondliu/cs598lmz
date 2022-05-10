import bz2
bz2.decompress(bz2_data)

# bz2.BZ2Compressor() bz2.BZ2Decompressor()

# gzip
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.crc32(s)

import struct
struct.pack('>I', 10240099)

x = zlib.decompress(t)
x

# lzma

