from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 2.2.2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 2.2.3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(b'\x01\x00\x00\x00')

# 2.2.4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(b'\x01\x00\x00\x00')
s.unpack_from(b'\x01\x00\x00\x00', 0)

# 2.2.5
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.unpack(b'\x01
