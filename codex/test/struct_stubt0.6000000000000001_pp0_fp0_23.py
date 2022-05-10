from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# _struct.Struct.pack()
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack_into(1)

# _struct.Struct.size()
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# _struct.Struct.unpack()
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(1)

# _struct.Struct.unpack_from()
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(1)

# _struct.pack()
from _struct import pack
pack('i')

# _struct.unpack()
from _struct import unpack
unpack('i')

# _testcapi.test_lazy_hash_inheritance()
