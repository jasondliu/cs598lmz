from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">H"
s.size = calcsize(s.format)
