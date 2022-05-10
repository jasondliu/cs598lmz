from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x9a\x99\x99\x99\x99\x9a'))

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I 2s f')
print(s.size)
print(s.pack(1, b'ab', 2.7))
print(s.unpack(b'\x00\x00\x00\x01ab\x00\x00\x9a\x99\x99\x99\x99\x9a'))
