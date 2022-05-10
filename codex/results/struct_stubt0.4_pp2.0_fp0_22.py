from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import sys
sys.getsizeof(s)

s.pack(1, False, 3.14159)

s.unpack(_)

s.pack(1, True, 3.14159)

s.unpack(_)

s.pack(1, 3.14159)

s.unpack(_)

s = Struct('iif')
s.unpack(_)

s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00@\t@')

s.unpack(b'\x01\x00\x00\x00\x01\x00\x00\x00\x00@\t@')

s.pack(1, True, 2.71828)

s.pack(1, False, 2.71828)

import struct
struct.pack('>I', 10240099)


