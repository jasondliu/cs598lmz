from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01', 0)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 0)

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)

s.pack_into(b'\x00'*8, 4, 2)

b

s.unpack_from(b, 4)

s = Struct('iif')
s.size

s.pack(1, 2, 3.0)

s.unpack(_)

