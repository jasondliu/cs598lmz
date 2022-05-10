from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(0)
s.pack('abc')
