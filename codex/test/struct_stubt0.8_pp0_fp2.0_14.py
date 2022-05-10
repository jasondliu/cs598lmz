from _struct import Struct
s = Struct.__new__(Struct)
print(s.pack('hhhh', 1, 2, 3, 4))
