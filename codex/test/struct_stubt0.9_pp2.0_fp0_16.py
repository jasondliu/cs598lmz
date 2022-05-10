from _struct import Struct
s = Struct.__new__(Struct)
s.format = ">iii"
d = s.unpack_from("hhhh", "foo")
