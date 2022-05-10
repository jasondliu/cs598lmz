from _struct import Struct
s = Struct.__new__(Struct)
s.format = "P"
s.size = 8
b = s.pack(100)
s.pack_into(b, 0, 100)
print(b)
