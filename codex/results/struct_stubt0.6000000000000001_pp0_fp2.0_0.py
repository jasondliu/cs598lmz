from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<hhl')
print(s.pack(1, 2, 3))
print(s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03'))
print(s.size)
print(s.format)
print(s.unpack_from(b'\x00\x01\x00\x02\x00\x00\x00\x03', 4))
print(s.unpack_from(b'\x00\x01\x00\x02\x00\x00\x00\x03'))
