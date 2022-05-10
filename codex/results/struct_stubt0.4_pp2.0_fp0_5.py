from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

s.pack(1)

s.unpack(_)

s.unpack(_[::-1])

s.unpack_from(_[::-1], 0)

s.unpack_from(_[::-1], 1)

import array
a = array.array('i', range(5))
a

a.tostring()

s.pack(a[0])

s.pack(a[1])

s.pack(a[2])

s.pack(a[3])

s.pack(a[4])

s.pack_into(a, 0, 1)

a

s.pack_into(a, 1, 2)

a

s.pack_into(a, 2, 3)

a

s.pack_into(a, 3, 4)

a

s.pack_into(a, 4, 5)

a

s.unpack(a.tostring())

s.unpack
