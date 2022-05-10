from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

s.pack(1)

s.pack(2)

s.pack(3)

s.pack(4)

s.pack(5)

s.pack_into(bytearray(4), 0, 6)

s.pack_into(bytearray(4), 0, 7, 8)

s.unpack(b'\x01\x00\x00\x00')

s.unpack_from(bytearray(b'\x01\x00\x00\x00'), 0)

s.unpack_from(bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00'), 0)

s.unpack_from(bytearray(b'\x01\x00\x00\x00\x02\x00\x00\x00'), 4)

import _struct
_struct.calcsize('i')

_struct.pack('i', 1)

