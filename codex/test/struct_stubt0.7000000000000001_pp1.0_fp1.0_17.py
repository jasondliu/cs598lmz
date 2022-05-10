from _struct import Struct
s = Struct.__new__(Struct)
for i in xrange(5): s.pack(i)
