from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i 4s f'
s.size = s.calcsize(s.format)
