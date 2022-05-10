from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)
s.pack(1, 2)

# _struct.Struct.pack_into
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack_into(b'', 0, 1)
s.pack_into(b'', 0, 1, 2)

# _struct.Struct.unpack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01')
s.unpack(b'\x01\x02')

# _struct.Struct.unpack_from
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'\x01')
s.unpack_from(b'\x01\x02')

# _struct.Struct.iter_unpack
from _struct import Struct
s = Struct.__new__(Struct)
s
