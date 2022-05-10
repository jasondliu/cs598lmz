from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'b'
s.size = 1
s.unpack(b'B')
# (66,)
