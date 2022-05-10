from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.size

# 2.2.2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack(1)

# 2.2.3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack(b'\x01\x00')

# 2.2.4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack(b'\x01\x00')[0]

# 2.2.5
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.pack_into(b'\x00'*2, 0, 1)

# 2.2.6
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
s.unpack_
