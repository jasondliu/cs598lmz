from _struct import Struct
s = Struct.__new__(Struct)
print(s.pack(b'hhl', 1, 2, 3))
