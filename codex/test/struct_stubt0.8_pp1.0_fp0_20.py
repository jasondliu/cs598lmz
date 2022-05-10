from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = struct.calcsize(s)
print(s.size)
print(s.format)
