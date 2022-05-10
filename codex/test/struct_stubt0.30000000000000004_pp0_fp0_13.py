from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# or

from _struct import Struct
Struct('i').pack(1)

# or

from _struct import pack
pack('i', 1)
