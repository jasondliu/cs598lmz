from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

s.pack(1)

s.unpack(b'\x00\x00\x00\x01')

s.unpack_from(b'\x00\x00\x00\x01')

s.unpack_from(b'\x00\x00\x00\x01', 4)

s.unpack_from(b'\x00\x00\x00\x01', 0)

s.unpack_from(b'\x00\x00\x00\x01', 1)

s.unpack_from(b'\x00\x00\x00\x01', 2)

s.unpack_from(b'\x00\x00\x00\x01', 3)

s.unpack_from(b'\x00\x00\x00\x01', 5)

s.unpack_from(b'\x00\x00\x00\x01', 6)

s.un
