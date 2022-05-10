from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__('i?f', False)
print(s.size)

# s = Struct('i?f')
# print(s.size)

# print(s.pack(1, False, 3.14159))
# print(s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'))
