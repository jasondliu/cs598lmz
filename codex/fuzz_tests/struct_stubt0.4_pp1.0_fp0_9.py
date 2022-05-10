from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# Python 3.x
from struct import Struct
s = Struct('>I')
s.unpack(b'\x00\x00\x00\x01')

# Python 3.x
from struct import unpack
unpack('>I', b'\x00\x00\x00\x01')
