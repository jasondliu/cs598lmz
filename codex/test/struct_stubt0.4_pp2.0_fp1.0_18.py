from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
struct.calcsize('i?f')

octets = b'\x01\x02\x03\x04'
s.unpack(octets)

data = s.pack(1, False, 3.14159)
data

s.unpack(data)

s = Struct('>i?f')
s.unpack(data)

s = Struct('<i?f')
s.unpack(data)

s = Struct('i?f')
s.unpack(data)

s = Struct('i?f')
s.unpack_from(data, 1)

s = Struct('i?f')
s.unpack_from(data, 2)

s = Struct('i?f')
s.unpack_from(data, 3)

s = Struct('i?f')
s.unpack_from(data, 4)

s = Struct('i?f')
