from _struct import Struct
s = Struct.__new__(Struct)
print s
s.format = 'iif'
print s.size

print Struct('i').unpack('\x01\x00\x00\x00')
print Struct('i').unpack_from('\x00\x00\x00\x01\x00\x00\x00\x02', 4)
print Struct('i').pack_into('\x00\x00\x00\x01', '\x00\x00\x00\x00\x00\x00\x00\x02', 4)
print Struct('i').pack('\x01')

import struct
import sys

print struct.calcsize('P') * 8
print struct.pack('i', 10240099)
print struct.unpack('i', '\x00\x9c@c')
print struct.pack('ii', 1, 2)
print struct.unpack('ii', '\x00\x00\x00\x01\x00\x00\x00\x02')
print struct.unpack('i', '\x00\x
