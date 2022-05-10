from _struct import Struct
s = Struct.__new__(Struct)
s.size=lambda: 8
print(s.size())
