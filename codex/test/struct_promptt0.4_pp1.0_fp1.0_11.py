import _struct
# Test _struct.Struct

import struct
from test import support

# Some structs to test with

# format 'x' not supported
FORMATS = 'bBhHiIlLqQfd'

# All are native, since we are testing the native module
NATIVE_FORMATS = FORMATS + '@='

# The number of bytes required to store the above formats
LENGTHS = (1, 1, 2, 2, 4, 4, 4, 8, 8, 8, 8, 1)

# The number of bytes required to pack the above formats
PACKLEN = (1, 1, 2, 2, 4, 4, 4, 8, 16, 8, 16, 0)

# The default values for each format
VALUES = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, 0)

# The byte order to pack the above formats with
ENDIANNESS = ('@', '=', '<', '>', '!')

# The alignment of each format
