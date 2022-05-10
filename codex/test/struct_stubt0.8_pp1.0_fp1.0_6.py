from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'II3s'
s.size = s.calcsize(s.format)
