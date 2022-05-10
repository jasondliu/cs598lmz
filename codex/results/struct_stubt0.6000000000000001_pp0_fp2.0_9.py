from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>HHH')
print(s.size)
print(s.pack(65534, 0, 5))

import struct
print(struct.pack('>HHH', 65534, 0, 5))
