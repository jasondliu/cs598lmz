from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x01', 0)

s.unpack_from(b'\x00\x01\x02\x03', 2)

s.unpack_from(b'\x00\x01\x02\x03', 1)

import array
a = array.array('H', [1, 2, 3, 4, 5, 6])
a

a.tobytes()

s.pack_into(a, 0, 7)

a

s.pack_into(a, 2, 8)

a

s.unpack_from(a, 4)

s.pack(1, 2, 3)

s.pack_into(a, 0, *range(10))

a

s.unpack_from(a, 0)

s.unpack_from(a, 2)

s.unpack_from(a, 4
