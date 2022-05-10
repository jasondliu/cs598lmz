from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>B')

s.pack(1)

# s.pack(1, 2)
# TypeError: pack() takes exactly 1 argument (2 given)


s.unpack(b'\x01')
# (1,)

s.unpack(b'\x01\x02')
# TypeError: unpack() takes exactly 1 argument (2 given)


s.format
# '>B'

s.size
# 1

s.pack_into(b'\x00' * s.size, 0, 1)
# None

b
# bytearray(b'\x01')

import struct

# pack_into and unpack_from are exact opposite of each other
struct.pack_into('>B', b, 0, 1)

b
# bytearray(b'\x01')

struct.unpack_from('>B', b)
# (1,)
