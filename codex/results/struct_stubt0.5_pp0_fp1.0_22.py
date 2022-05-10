from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s = Struct('i')
s.size

import struct
# struct.__init__()
struct.calcsize('i')

import struct
struct.calcsize('P') * 8

import struct
struct.pack('i', 10240099)

import struct
struct.unpack('i', b'\x00\x9c@c')

import struct
struct.unpack('>I', b'\x00\x9c@c')

import struct
struct.pack('>I', 10240099)

import struct
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

import struct
for x in range(0, 32):
    print(x, struct.pack('>I', x ** 2))

import hashlib
md5 = hashlib.md5()
md5.update(b'how to use md5 in python hashlib?')
md5.hexdigest()

import hashlib

