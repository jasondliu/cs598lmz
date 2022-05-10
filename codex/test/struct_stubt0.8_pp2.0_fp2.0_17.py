from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__['format'] = 'I H'
s.__dict__['size'] = s.size
print(s.size)
print(s.format)
print(s.unpack_from(b'\x00\x00\x00\x08\x00\x00', 4))
# => (524288, 0)

print(s.unpack_from(b'\x00\x00\x00\x08\x00\x00'))
# => (8, 0)
