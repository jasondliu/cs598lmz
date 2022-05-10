from _struct import Struct
s = Struct.__new__(Struct)
s. format = '&lt;BH'
s.size = s.calcsize(s.format) # 5
