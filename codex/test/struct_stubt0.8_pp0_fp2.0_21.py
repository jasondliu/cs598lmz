from _struct import Struct
s = Struct.__new__(Struct)
s

s = Struct('i?f')
s

s = Struct('i?f')
s.size

s = Struct('i?f')
s.format

s = Struct('i?f')
s.unpack(b' \x00\x00\x00\x00\x00\x00\x00@\t\x00\x00')

s = Struct('i?f')
s.unpack_from(b' \x00\x00\x00\x00\x00\x00\x00@\t\x00\x00')

s = Struct('i?f')
s.pack(1, True, 2.75)

s.unpack(_)

s.pack_into(bytearray(12), 0, 1, True, 2.75)

s.size
