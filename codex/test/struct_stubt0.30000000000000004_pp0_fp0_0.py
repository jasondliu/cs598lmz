from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# test pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
b = bytearray(s.size * 2)
s.pack_into(b, 0, 1)
s.pack_into(b, s.size, 2)
b

# test pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
b = bytearray(s.size * 2)
s.pack_into(b, 0, 1)
s.pack_into(b, s.size, 2)
s.unpack_from(b, 0)

# test pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
b = bytearray(s.size * 2)
s.pack_into(b, 0, 1)
s.pack_into(b, s.size, 2)
