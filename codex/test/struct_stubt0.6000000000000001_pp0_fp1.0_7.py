from _struct import Struct
s = Struct.__new__(Struct)
s.format = '2s f'
s.size = s.calcsize(s.format)
