from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# method 2
from _struct import Struct
Struct('i').unpack(b'\x01\x00\x00\x00')

# method 3
from _struct import unpack
unpack('i', b'\x01\x00\x00\x00')

# method 4
from _struct import unpack_from
unpack_from('i', b'\x01\x00\x00\x00')

# method 5
from _struct import unpack_from
unpack_from('i', b'\x01\x00\x00\x00', 0)

# method 6
from _struct import unpack_from
unpack_from('i', b'\x01\x00\x00\x00', 0, 1)

# method 7
from _struct import unpack_from
