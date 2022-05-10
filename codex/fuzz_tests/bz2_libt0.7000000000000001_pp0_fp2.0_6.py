import bz2
bz2.compress(bytes(h, 'ascii'))

bz2.decompress(bytes(h, 'ascii'))

import bz2
bz2.compress(bytes('hello world!', 'ascii'))

import json

json.dumps([1, 'simple', 'list'])

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

import struct

struct.pack('>i4sh', 7, b'spam', 8)

struct.unpack('>i4sh', b'\x00\x00\x00\x07spam\x00\x08')

import struct
# struct format: > - big endian, i - int, 4 - 4 bytes, l - long, q
