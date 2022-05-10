from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda : 1
#print hex(id(s))
#print hex(id(s.size))
#print hex(id(s.size()))
