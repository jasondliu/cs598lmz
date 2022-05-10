from _struct import Struct
s = Struct.__new__(Struct)
print(s)

print(s.pack(b'hhl', 1, 2, 3))
print(s.unpack(b'\x00\x01\x00\x02\x00\x00\x00\x03', b'hhl'))

print(s.calcsize(b'hhl'))

print(s.pack_into(b'hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03', 1, 2, 3))
print(s.unpack_from(b'\x00\x01\x00\x02\x00\x00\x00\x03', b'hhl', 0))
