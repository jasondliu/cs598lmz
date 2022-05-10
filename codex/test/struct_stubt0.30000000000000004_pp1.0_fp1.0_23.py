from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

s.pack(123)

s.unpack(b'\x00\x00\x00{')

s.unpack(b'\x00\x00\x00{')[0]

s.unpack_from(b'\x00\x00\x00{')

s.unpack_from(b'\x00\x00\x00{', 0)

s.unpack_from(b'\x00\x00\x00{', 0)[0]

s.unpack_from(b'\x00\x00\x00{', 4)

s.unpack_from(b'\x00\x00\x00{', 4)[0]

s.unpack_from(b'\x00\x00\x00{', 5)

s.unpack_from(b'\x00\x00\x00{', 5)[0]

