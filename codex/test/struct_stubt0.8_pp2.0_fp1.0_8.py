from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<15sh'
s.size = s.unpack(bytes(30)).__sizeof__()
print(s.size)
