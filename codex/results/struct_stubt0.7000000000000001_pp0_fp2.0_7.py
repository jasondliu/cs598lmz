from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'

print(s.unpack(b'1')[0])
