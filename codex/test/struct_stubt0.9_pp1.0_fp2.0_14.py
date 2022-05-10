from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I i'
s.size = struct.calcsize(s.format)
