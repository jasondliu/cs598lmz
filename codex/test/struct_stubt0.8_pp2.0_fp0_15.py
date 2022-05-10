from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>4s2h2f')
data = s.pack(*('abcd', 2, 1, 2, 1.1))
print(data)
print(s.unpack(data))
