from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00')

# Deserialization
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00')
