from _struct import Struct
s = Struct.__new__(Struct)
print(s)

s.format = '>I'
