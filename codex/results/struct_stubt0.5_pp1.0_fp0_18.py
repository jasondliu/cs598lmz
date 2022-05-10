from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('H')
s.size

s.unpack(b'\x01\x02')

s.unpack_from(b'\x01\x02', 0)

s.unpack_from(b'\x01\x02\x03\x04', 2)

s.pack(1)

s.pack_into(b'\x00' * s.size, 0, 1)

s.pack_into(b'\x00' * s.size, 2, 1)

s.pack_into(b'\x00' * 4, 2, 1)

s.unpack_from(b'\x00' * 4, 2)

s.pack_into(b'\x00' * 4, 2, 1)

s.unpack_from(b'\x00' * 4, 2)

s.pack_into(b'\x00' * 4, 2, 1)

s.unpack_from(b'\x00' * 4, 2)


#
