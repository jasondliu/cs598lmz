from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

import struct
struct.calcsize('I 2s f')

octets = s.pack(1, b'ab', 2.7)
octets

s.unpack(octets)

octets = b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@\x00\x00\x00'
s.unpack(octets)

octets = b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@\x00\x00\x00'
s.unpack_from(octets, 4)

octets = b'\x01\x00\x00\x00ab\x00\x00\x00\x00\x00\x00@\x00\x00\x00'
s.unpack_from(octets, 4)

