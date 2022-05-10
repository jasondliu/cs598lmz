from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x01', 0)

s.unpack_from(b'\x00\x01\x02\x03', 2)

s.pack_into(b'\x00\x00\x00\x00', 2, 3)

b

s.pack_into(b'\x00\x00\x00\x00', 2, 3, 4)

b

import array
a = array.array('H', [1, 2, 3, 4])
a

a.tobytes()

a.tobytes() == a.tostring()

a.frombytes(b'\x00\x01\x02\x03')

a

a.frombytes(b'\x00\x01\x02\x03\x04\x05')

a

a.byteswap()

a

a
