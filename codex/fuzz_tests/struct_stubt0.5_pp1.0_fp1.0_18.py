from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')

print(s.size)
print(s.pack(1))
print(s.pack(1)[0])
print(s.unpack(b'\x00\x00\x01\x00'))
print(s.unpack(b'\x00\x00\x01\x00')[0])
