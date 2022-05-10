from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x01')

# Method 2:
from _struct import Struct
Struct('i').unpack(b'\x00\x00\x00\x01')

# Method 3:
from _struct import unpack_from
unpack_from('i', b'\x00\x00\x00\x01')

# Method 4:
from _struct import unpack
unpack('i', b'\x00\x00\x00\x01')

# Method 5:
import struct
struct.unpack('i', b'\x00\x00\x00\x01')

# Method 6:
import struct
struct.Struct('i').unpack(b'\x00\x00\x00\x01')

# Method 7:
import struct
struct.unpack_from('i', b'\x00\x00\x00\x01')

# Method 8:
import struct
struct.Struct('i').unpack
