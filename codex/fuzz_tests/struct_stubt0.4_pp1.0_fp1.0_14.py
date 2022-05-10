from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

import struct
s = struct.Struct('i?f')
s.size

s = struct.Struct('i?f')
s.pack(1, False, 2.3)

s.unpack(_)

s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@')

s.unpack_from(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@', 4)

s = struct.Struct('i?f')
s.pack_into(bytearray(s.size), 0, 1, False, 2.3)

s.unpack_from(_, 0)

s.unpack_from(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@',
