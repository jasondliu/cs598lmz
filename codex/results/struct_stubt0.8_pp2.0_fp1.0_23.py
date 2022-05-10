from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# s.pack(*[1, True, 2.3])
# s.pack(1, True, 2.3)
# s.pack(1, False, 2.3)

print(s.pack(1, True, 2.3))
print(s.unpack(b'\x01\x01\x00\x00\x00?\x99\x99\x99\x99\x99\x9a'))
print(s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00?\x99\x99\x99\x99\x99\x9a'))
