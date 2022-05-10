from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# Python 2.7.3
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# Python 3.2.3
from _struct import Struct
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x01')

# Python 3.2.3
from _struct import Struct
s = Struct('>i')
s.unpack_from(b'\x00\x00\x00\x01')

# Python 2.7.3
s = Struct('>i')
s.unpack_from(b'\x00\x00\x00\x01')

# Python 3.2.3
from _struct import Struct
s = Struct('>i')
s.unpack_from(b'\x00\x00\x00\x01')

# Python 3.2.3

