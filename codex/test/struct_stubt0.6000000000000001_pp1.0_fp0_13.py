from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
f = s.unpack_from
