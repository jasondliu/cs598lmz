from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'bBhlLfdsp?'
s.size = struct.calcsize(s.format)
