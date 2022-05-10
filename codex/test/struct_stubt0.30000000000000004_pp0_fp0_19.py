from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x01', 0)

s.unpack_from(b'\x00\x01\x02\x03', 1)

s.unpack_from(b'\x00\x01\x02\x03', 1, 2)

import array
a = array.array('i', range(5))
a

a.tostring()

s.pack(1)

s.pack_into(a, 0, 1)

a

s.pack_into(a, 1, 2)

a

s.unpack_from(a, 0)

s.unpack_from(a, 1)

s.unpack_from(a, 1, 2)

import struct
struct.pack('>H', 1)

struct.pack('>H', 1)

struct.unpack('>H', _)
