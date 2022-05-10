from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x00')

# Method 2:
from _struct import Struct
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x00')

# Method 3:
from _struct import unpack
unpack('>i', b'\x00\x00\x00\x00')

# Method 4:
from _struct import unpack_from
unpack_from('>i', b'\x00\x00\x00\x00', 0)

# Method 5:
from _struct import unpack_from
unpack_from('>i', b'\x00\x00\x00\x00', 0)

# Method 6:
from _struct import unpack_from
unpack_from('>i', b'\x00\x00\x00\x00', 0)

# Method 7:
from _struct import unpack_from
