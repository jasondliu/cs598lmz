from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 3.2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', True)
s.size

# 3.3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', True)
s.pack(1)

# 3.4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', True)
s.pack(1)
s.pack(2)

# 3.5
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', True)
s.pack(1)
s.pack(2)
s.pack(3)
s.unpack(b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03')

# 3.6
from _struct import Struct
