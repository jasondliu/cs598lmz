from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">L"
d = s.unpack(x)[0]
