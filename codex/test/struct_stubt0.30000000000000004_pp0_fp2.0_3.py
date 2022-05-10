from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.pack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# struct.Struct.unpack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.unpack_from
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01\x00\x00\x00', 0)

# struct.Struct.iter_unpack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.iter_unpack(b'\x01\x00\x00\x00')

# struct.Struct.format
from _struct import Struct
s = Struct.__
