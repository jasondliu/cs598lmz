from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# issue14962
import _struct
_struct.Struct(b'i').pack(1)

# issue14963
import _struct
_struct.Struct(b'i').unpack(b'\x01\x00\x00\x00')

# issue14964
import _struct
_struct.Struct(b'i').unpack_from(b'\x01\x00\x00\x00')

# issue14965
import _struct
_struct.Struct(b'i').size

# issue14966
import _struct
_struct.Struct(b'i').format

# issue14967
import _struct
_struct.Struct(b'i').__new__(_struct.Struct)

# issue14968
import _struct
_struct.Struct(b'i').__init__(b'i')

# issue14969
import _struct
_struct.Struct(b'i').__repr__()

# issue14970
import _struct
