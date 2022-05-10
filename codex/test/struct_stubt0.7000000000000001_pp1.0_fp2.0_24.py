from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'abc'
s.size = s.calcsize()
s.unpack(b'abc')
# ('a', 'b', 'c')
