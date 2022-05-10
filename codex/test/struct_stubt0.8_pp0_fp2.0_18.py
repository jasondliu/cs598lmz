from _struct import Struct
s = Struct.__new__(Struct)
s.format = "%8s%3s"
s1 = s.pack(b"abc\0def", 1)
print(s1)
print(s.size)
print(s.unpack(s1))
