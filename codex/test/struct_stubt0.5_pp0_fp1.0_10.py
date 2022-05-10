from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
print(s.size)
print(s.pack(1))
print(s.pack_into(b'', 0, 1))
print(s.unpack(b'\x01\x00\x00\x00'))
print(s.unpack_from(b'\x01\x00\x00\x00', 0))

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<2i')
print(s.size)
print(s.pack(1, 2))
print(s.pack_into(b'', 0, 1, 2))
print(s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00'))
print(s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 0))

from _struct import Struct
