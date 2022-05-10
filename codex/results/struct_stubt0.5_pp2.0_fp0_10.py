from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<2s2s2s2s')
print s.size

print s.pack('a','b','c','d')
