from _struct import Struct
s = Struct.__new__(Struct)
print(s)
s.__init__('I 2s f')
print(s)
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x08@'))
print(s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x08@', 4))
