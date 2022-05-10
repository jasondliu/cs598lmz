from _struct import Struct
s = Struct.__new__(Struct)
s.size = 5
decode("test", s)
