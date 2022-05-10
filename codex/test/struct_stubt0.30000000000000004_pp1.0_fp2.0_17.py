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
s.unpack(s.pack(1))

# struct.Struct.unpack_from
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(s.pack(1), 0)

# struct.Struct.iter_unpack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
list(s.iter_unpack(s.pack(1)))

# struct.Struct.size
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# struct.Struct.
