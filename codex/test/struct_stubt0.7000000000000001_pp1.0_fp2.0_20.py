from _struct import Struct
s = Struct.__new__(Struct)  # empty structure
s.format = 'hhl'     # 2 short ints and a long
s.size = s.calcsize()
