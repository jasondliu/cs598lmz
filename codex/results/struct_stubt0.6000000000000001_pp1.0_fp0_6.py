from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s = Struct('i') # Two equivalent ways to create a Struct
s.size

s = Struct('i?f')
s.size

s.pack(1, True, 2.3)

s.unpack(_)

s.pack(1, False, 2.3)

s.unpack(_)

s.unpack(b'\x01\x00\x00\x00\x01?\x9a\x99\x99\x99\x99\x9a')

s.unpack(b'\x01\x00\x00\x00\x00@\t\x1e-\xf3\xb6\x0e')

s.pack_into(bytearray(12), 3, 1, False, 2.3)

memoryview(_)

s.unpack_from(_, 3)

s = Struct('iif')

s.pack(1, 2, 3.0)

s.unpack(_)

