from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.format)
print(s.pack(1))
print(s.unpack(b'\x01\x00\x00\x00'))
print(s.unpack_from(b'\x01\x00\x00\x00'))
print(s.unpack_from(b'\x01\x00\x00\x00', 0))

import struct
print(struct.unpack('i', b'\x01\x00\x00\x00'))
print(struct.unpack('i', b'\x01\x00\x00\x00', 0))

import sys
print(sys.byteorder)

print(struct.pack('i', 1))
print(struct.pack('i', 1)[::-1])

print(struct.pack('i', 1)[::-1].decode('latin-1'))
print(struct.pack('i', 1)[::-1].decode('latin-1').encode
