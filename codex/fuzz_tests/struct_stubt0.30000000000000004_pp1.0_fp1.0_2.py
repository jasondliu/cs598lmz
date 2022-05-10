from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x01', 0)

s.unpack_from(b'\x00\x01\x02\x03', 2)

s.pack_into(b'\x00\x00\x00\x00', 2, 7)

b

import array
a = array.array('i', b'\x01\x00\x02\x00\x03\x00')
a

a.tolist()

a = array.array('i', [1, 2, 3])
a

bytes(a)

import binascii
binascii.hexlify(a)

a = array.array('i', range(3))
a

a.tostring()

a.tostring() == bytes(a)

a.fromstring(b'\x00\x00\x00\x07\x08
