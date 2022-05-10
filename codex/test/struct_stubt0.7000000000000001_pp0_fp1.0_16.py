from _struct import Struct
s = Struct.__new__(Struct)
s.format = "i"
s.size = 4
s = Struct()
s.format = "i"
s.size = 4
class A(Struct):
    format = "i"
s = A()
s.format
#s.size = 4
s = Struct("i")
s.format
s.size
s = Struct()
s.format = "i"
s.size
s = Struct("i")
s.format = "i"
s = Struct("i")
s.unpack("\x01\x00\x00\x00")
s = Struct("ii")
s.format
s.size
s.unpack("\x01\x00\x00\x00\x02\x00\x00\x00")
s.unpack("\x01\x00\x00\x00\x02")
s.unpack("")
s.unpack("\x01\x00\x00\x00")
s = Struct("i")
