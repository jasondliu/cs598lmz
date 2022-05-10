from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 2.2.2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)

# 2.2.3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')

# 2.2.4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')
s.unpack_from(b'\x00\x00\x00\x01', 0)

# 2.2.5
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.pack(1)
