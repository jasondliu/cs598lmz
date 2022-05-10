from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

s = Struct('i?f')
s.size

import struct
struct.calcsize('i?f')

octets = struct.pack('i?f', 1, False, 0.1)
octets

struct.unpack('i?f', octets)

octets = struct.pack('>i?f', 1, False, 0.1)
octets

octets = struct.pack('<i?f', 1, False, 0.1)
octets

struct.unpack('>i?f', octets)

struct.unpack('<i?f', octets)

octets = struct.pack('i?f', 1, False, 0.1)
octets

struct.unpack('i?f', octets)

octets = struct.pack('>i?f', 1, False, 0.1)
octets

octets = struct.pack('<i?f', 1, False, 0.1)
octets

struct.un
