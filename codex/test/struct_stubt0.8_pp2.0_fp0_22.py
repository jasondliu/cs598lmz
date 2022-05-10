from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s4s4s4s4s4s4s4s' # (new string)
s.size = Struct.calcsize(s.format) # (new method)
