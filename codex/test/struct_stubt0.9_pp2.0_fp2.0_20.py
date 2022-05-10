from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hhl'
s.size = calcsize(s.format)
t = (1, 2, 3)
