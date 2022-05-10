from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2I'
s.size = 8
print(s.pack(1,2))
print(s.unpack(s.pack(1,2)))
print(s.unpack_from(s.pack(1,2),0))

s = Struct.__new__(Struct)
s.format = '>2I'
s.size = 8
print(s.pack(1,2))
print(s.unpack(s.pack(1,2)))
print(s.unpack_from(s.pack(1,2),0))

s = Struct.__new__(Struct)
s.format = '@2I'
s.size = 8
print(s.pack(1,2))
print(s.unpack(s.pack(1,2)))
print(s.unpack_from(s.pack(1,2),0))

s = Struct.__new__(Struct)
s.format = '=2I'
s.size = 8
print(s.pack(1,2))
