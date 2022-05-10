from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i")

print s.size

print s.pack(1)

print s.pack_into(buffer(bytearray(4)), 0, 1)

print s.unpack(s.pack(1))

print s.unpack_from(buffer(bytearray(s.pack(1))), 0)
