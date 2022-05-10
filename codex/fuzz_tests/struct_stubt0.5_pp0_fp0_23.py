from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x03')

# 3.2
from struct import Struct
s = Struct('>i')
s.unpack(b'\x00\x00\x00\x03')

# 3.3
from struct import unpack
unpack('>i', b'\x00\x00\x00\x03')

# 3.4
from struct import Struct
s = Struct('>i')
s.unpack_from(b'\x00\x00\x00\x03', 0)

# 3.5
from struct import unpack_from
unpack_from('>i', b'\x00\x00\x00\x03', 0)

# 3.6
from struct import Struct
s = Struct('>i')
s.pack(3)

# 3.7
from struct import pack
pack('>i', 3)

# 3.8
from struct import Struct
s = Struct('>i')
s
