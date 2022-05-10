from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bb')
s.size
s.pack(1,2)
b = bytes(s.pack(1,2))
b
s.unpack(b)
s.unpack_from(b)
m = memoryview(b)
s.unpack_from(m)
m2 = m[:2]
m2
s.unpack_from(m2)
