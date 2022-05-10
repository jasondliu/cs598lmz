import bz2
bz2.decompress(compressed_data)

import gzip
s = b'witch which has which witches wrist watch'
len(s)

t = gzip.compress(s)
len(t)

gzip.decompress(t)

import zlib
len(zlib.compress(s))
len(zlib.decompress(zlib.compress(s)))

# zlib.decompress(zlib.compress(s))

# zlib.crc32(s)

import binascii
binascii.crc32(s)

import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# struct.pack('>IH', 10240099, 10240099)

# struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# struct.pack('>IH', 1024
