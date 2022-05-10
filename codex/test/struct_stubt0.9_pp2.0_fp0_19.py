from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">xI"
buf = "\x00spam\x00"
