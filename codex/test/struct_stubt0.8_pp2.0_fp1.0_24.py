from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

data = s.pack(1, False, 0.5)
print(data)

import sys
sys.byteorder

l = list(s.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8?\x00\x00\x00\x00\x00\x00'));
l

import struct
struct.Struct.__new__(struct.Struct, 'i')
struct.Struct.__new__(struct.Struct, 'i').size
struct.Struct.__new__(struct.Struct, 'i').pack(1)
struct.Struct.__new__(struct.Struct, 'i').unpack(b'\x01\x00\x00\x00')
