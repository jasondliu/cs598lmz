from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.size

s.pack(1)

s.unpack(_)

s.unpack(s.pack(1))

s.pack_into(buffer(bytearray(4)), 0, 1)

s.unpack_from(buffer(bytearray(4)), 0)

s.unpack_from(buffer(bytearray(4)), 0)

s = Struct.__new__(Struct)
s.__init__('i')
s.size

s.pack(1)

s.unpack(_)

s.unpack(s.pack(1))

s.pack_into(buffer(bytearray(4)), 0, 1)

s.unpack_from(buffer(bytearray(4)), 0)

s.unpack_from(buffer(bytearray(4)), 0)

s = Struct.__new__(Struct)
s.__init__('f')
s.size

s.pack(1)

s.
