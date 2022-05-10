from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s.format)
