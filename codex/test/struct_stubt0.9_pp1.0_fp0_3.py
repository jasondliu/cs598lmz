from _struct import Struct
s = Struct.__new__(Struct)
s.format = f
s.size = 24
s.unpack(buffer)
