from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<bb', 'xx')
print s.size
print s.pack(1, 2)
print s.unpack(s.pack(1,2))
print s.unpack_from(s.pack(1,2), 1)
print s.unpack_from(s.pack(1,2), 1,1)
print s.unpack_from(s.pack(1,2), 1,2)
print s.unpack_from(s.pack(1,2), 1,3)
