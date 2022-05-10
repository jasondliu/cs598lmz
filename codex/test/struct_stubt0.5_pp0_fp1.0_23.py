from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.pack(1)

# or

import struct
struct.pack('i',1)

# or

import array
array.array('i',[1]).tostring()
