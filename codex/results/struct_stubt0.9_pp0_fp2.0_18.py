from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>B'
s.size = s.format.__sizeof__()
s.unpack(b'\x68')[0]

from struct import Struct
Struct('>B').unpack(b'\x68')[0]

from struct import Struct
struct = Struct('>B')
struct.size
struct.unpack(b'\x68')[0]
