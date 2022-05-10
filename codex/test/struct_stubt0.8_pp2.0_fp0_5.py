from _struct import Struct
s = Struct.__new__(Struct)
fmt = 'I 2s f' # unsigned int, 2 char, float
s.format = fmt
