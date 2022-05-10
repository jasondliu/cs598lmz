from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.size

class Structure:
    _fields_ = [
        ('<I', 'I1'),
        ('<I', 'I2')
    ]

Structure.format

import binascii
binascii.hexlify(Structure.format)

binascii.hexlify(Structure.format.encode('utf-8'))

s = Struct(Structure.format)
s.size

s.pack(1, 2)

s.unpack(_)

s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00')

s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00')

s.unpack_from(_, 4)

s.unpack_from(_, 8)

s.pack_into(_, 0, 1, 2)

s.pack_into(_, 4, 3,
