from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 2.
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)

# 3.
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)
s.unpack(b'\x00\x01')

# 4.
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)
s.unpack(b'\x00\x01')
s.unpack(b'\x00\x01')[0]

# 5.
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.pack(1)
s.unpack(b'\x00\x01')
s.unpack(b'\x00\x01')[0]
s.pack
