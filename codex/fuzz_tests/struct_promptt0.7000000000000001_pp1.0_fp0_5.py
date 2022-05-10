import _struct
# Test _struct.Struct
import struct
# Test struct.Struct
from _struct import *
# Test * import
from struct import *

# Test struct.error
try:
    struct.pack('c' * 100, *range(100))
except struct.error:
    pass

# Test struct.pack_into
try:
    struct.pack_into('1024c', buffer(bytearray(1024)), 0, *range(1024))
except struct.error:
    pass

# Test struct.unpack_from
try:
    struct.unpack_from(str(1024) + 'c', buffer(bytearray(1024)), 0)
except struct.error:
    pass

# Test _struct.error
try:
    _struct.pack('c' * 100, *range(100))
except _struct.error:
    pass

# Test _struct.pack_into
try:
    _struct.pack_into('1024c', buffer(bytearray(1024)), 0, *range(1024))
except _struct.error:
    pass

# Test _struct.unpack
