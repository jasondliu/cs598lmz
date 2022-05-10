from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>IIII'
s.size = len(data)
values = s.unpack(data)
