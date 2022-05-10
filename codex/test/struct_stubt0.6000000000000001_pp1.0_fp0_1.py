from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<dd'
s.size = calcsize(s.format)
