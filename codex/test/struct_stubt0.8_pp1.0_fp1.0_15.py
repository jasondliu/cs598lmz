from _struct import Struct
s = Struct.__new__(Struct)  # new struct class
s.format = '>lhhl'  # big-endian long, short, short, long
s.size = s.calcsize(s.format)
