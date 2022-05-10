from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>16si')
s.unpack(buf)
# (b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 0)
