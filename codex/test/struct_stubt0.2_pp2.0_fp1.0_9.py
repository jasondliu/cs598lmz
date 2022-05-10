from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00'*4, 0)

s.unpack_from(b'\x00'*4, 4)

s.pack_into(b'\x00'*8, 4, 7)

s.unpack_from(_, 4)

s.pack(1, 2, 3)

s.unpack(_)

s.pack_into(b'\x00'*12, 0, 1, 2, 3)

s.unpack_from(_, 0)

s.unpack_from(_, 4)

s.unpack_from(_, 8)

s.pack(1, 2, 3, 4)

s.unpack(_)

s.pack_into(b'\x00'*16, 0, 1, 2, 3, 4)

s.unpack_from(_, 0)

