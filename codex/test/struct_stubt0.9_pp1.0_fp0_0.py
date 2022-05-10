from _struct import Struct
s = Struct.__new__(Struct)

s.size = s.__sizeof__()

print(s.size)
