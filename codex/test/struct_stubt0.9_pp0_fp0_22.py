from _struct import Struct
s = Struct.__new__(Struct)
_struct.Struct.__init__(s, '>l')
data = s.pack(_int)
