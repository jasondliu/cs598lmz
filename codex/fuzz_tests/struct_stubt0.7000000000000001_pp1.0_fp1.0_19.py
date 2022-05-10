from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HHI'
s.size = s.calcsize(s.format)
print(s.size)
print(s.pack(1,2,3))
print(s.unpack(s.pack(1,2,3)))
