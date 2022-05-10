from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.pack(1)

# test_unpack_from
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.unpack_from(b'\x01\x00', 0)

# test_unpack_from_buffer
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.unpack_from(bytearray(b'\x01\x00'), 0)

# test_pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
b = bytearray(2)
s.pack_into(b, 0, 1)

# test_unpack_from_buffer_too_short
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
try:
    s.unpack_from(b'\x01', 0)
except Exception as e:
