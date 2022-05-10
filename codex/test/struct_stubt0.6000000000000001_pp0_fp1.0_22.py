from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4

print(s.pack(1))
