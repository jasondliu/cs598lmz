from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# pack
s.pack(1, b'ab', 2.7)

# unpack
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')

# calcsize
s.calcsize(b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@\x9a\x99\x99\x99\x99\x9a')

# pack_into
buffer = bytearray(s.size)
s.pack_into(buffer, 0, 1, b'ab', 2.7)

# unpack_from
s.unpack_from(buffer, 0)

# Struct
Struct('I 2s f')
Struct(b'I 2s f')

# Struct.__
