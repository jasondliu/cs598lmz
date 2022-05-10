from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>BH'
s.size = 4
s.pack = Struct.pack.__get__(s)
s.unpack = Struct.unpack.__get__(s)

s.unpack(b'\x00\x00\x00\x00')
# (0, 0)
s.unpack(b'\x00\x00\x00\x01')
# (0, 1)
s.unpack(b'\x00\x00\x01\x00')
# (0, 256)
s.unpack(b'\x00\x01\x00\x00')
# (0, 65536)
s.unpack(b'\x01\x00\x00\x00')
# (1, 0)
s.unpack(b'\x01\x00\x00\x01')
