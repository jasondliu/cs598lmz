from _struct import Struct
s = Struct.__new__(Struct) # this is a call to Struct.__new__
s.format = '2i4sf' # attribute assignment
s.size = s.calcsize(s.format) # another attribute assignment
