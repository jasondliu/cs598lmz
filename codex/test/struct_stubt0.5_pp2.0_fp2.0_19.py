from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1

print(s.pack(255))
print(s.pack(256))
print(s.pack(257))

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1
print(s.unpack(b'\x00'))
print(s.unpack(b'\xff'))

print(s.unpack(b'\x00\x01'))

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1

print(s.unpack_from(b'\x00\x01'))
print(s.unpack_from(b'\x01\x00', 1))

s = Struct.__new__(Struct)
s.format = 'B'
s.size = 1

print(s.iter_unpack(b'\x00\x01'))
print(s.iter_unpack(b'\x01\x00', 1))
