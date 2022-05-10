from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
a = s.pack(1)
s.size = 8
s.pack(2)
