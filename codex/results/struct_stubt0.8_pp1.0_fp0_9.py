from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>h')
print s.size
print s.pack(1)
print s.unpack(s.pack(1))
print s.unpack(s.pack(1))[0]
