from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.unpack(b'\x01\x00\x00\x00'))
