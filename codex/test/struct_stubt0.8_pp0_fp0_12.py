from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
b = s.pack(2**31-1)
s2 = Struct.__new__(Struct)
s2.__init__(b)
s2.unpack(b)
