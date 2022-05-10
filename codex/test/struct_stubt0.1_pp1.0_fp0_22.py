from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01', 0)

s.unpack_from(b'\x00\x00\x00\x01', 4)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 0)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)

import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
a

s.pack_into(a, 0, 1)

a

s.pack_into(a, 4, 2)

a

s.unpack_from(a, 0)

s.unpack_from(a, 4)

s.un
