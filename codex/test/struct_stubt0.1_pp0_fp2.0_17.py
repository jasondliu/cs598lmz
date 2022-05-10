from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# _struct.Struct.unpack_from
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

# _struct.Struct.iter_unpack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.iter_unpack(b'\x01\x00\x00\x00')

# _struct.Struct.pack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack_into(b'\x00' * 4, 0, 1)

