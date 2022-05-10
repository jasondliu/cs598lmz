from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
s.size = s.calcsize('HH')
s.pack(1, 2)

s.unpack(b'\x01\x00\x02\x00')

s.unpack(b'\x01\x00\x02\x00')

s.unpack_from(b'\x01\x00\x02\x00', 0)

s.unpack_from(b'\x01\x00\x02\x00', 1)

s.unpack_from(b'\x01\x00\x02\x00', 0)

s.unpack_from(b'\x01\x00\x02\x00', 1)

s.unpack_from(b'\x01\x00\x02\x00', 1)

s.unpack_from(b'\x01\x00\x02\x00', 1)

