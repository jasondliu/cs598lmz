from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1, b'ab', 3.0))
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x80?\x00'))
