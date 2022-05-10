from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', 'f')
s.size

s.pack(1, 2.0)

s.unpack(_)

s.unpack_from(b'\x01\x00\x00\x00\x00\x00\x00\x00', 0)

s.unpack_from(b'\x01\x00\x00\x00\x00\x00\x00\x00', 1)

s.pack_into(b'\x00' * 8, 0, 1, 2.0)

b = bytearray(b'\x00' * 8)
s.pack_into(b, 0, 1, 2.0)
b

s.unpack_from(b, 0)

s.unpack_from(b, 1)

s.iter_unpack(b)

list(_)

s.iter_unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x02\
