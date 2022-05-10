from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x08\x00\x00\x00')

print(s.unpack(b'\x08\x00\x00\x00'))

print(s.unpack(b'\x00\x00\x00\x00'))

print(s.unpack_from(b'\x00\x00\x00\x00', 0))

print(s.unpack_from(b'\x00\x00\x00\x00', 1))
