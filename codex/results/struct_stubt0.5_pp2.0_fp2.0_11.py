from _struct import Struct
s = Struct.__new__(Struct)

s.__init__('i?f')

s.pack(1, False, 2.3)

s.unpack(_)

s.size

s = Struct('i?f')

s.pack(1, False, 2.3)

s.unpack(_)

s.size

s.pack(1, False, 2.3)

s.pack_into(bytearray(s.size), 0, 1, False, 2.3)

s.unpack_from(bytearray(s.size), 0)

s.pack(1, False, 2.3)

s.pack_into(bytearray(s.size), 0, *(1, False, 2.3))

s.unpack_from(bytearray(s.size), 0)

s = Struct('i?f')

s.unpack(s.pack(1, False, 2.3))

s = Struct('i?f')

s.unpack(s.pack(1, False, 2
