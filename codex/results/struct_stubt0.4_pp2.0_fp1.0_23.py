from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4
s.unpack_from(b'\x01\x00\x00\x00', 0)
(1,)
s.unpack_from(b'\x00\x00\x00\x01', 0)
(16777216,)
s.unpack_from(b'\x00\x00\x00\x02', 0)
(2,)
s.unpack_from(b'\x00\x00\x00\x03', 0)
(3,)
s.unpack_from(b'\x00\x00\x00\x04', 0)
(4,)
s.unpack_from(b'\x00\x00\x00\x05', 0)
(5,)
s.unpack_from(b'\x00\x00\x00\x06', 0)
(6,)
s.unpack_from(b'\x00\x00\x00\x07', 0)
(7,)
s.unpack
