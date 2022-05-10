from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'd'
s.size = 8
s.unpack('aaaaa')
