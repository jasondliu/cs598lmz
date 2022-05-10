from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("> i")
s.unpack(buffer("\x00\x00\x00\x0b", 4))
# (11,)
