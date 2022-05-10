import _struct
# Test _struct.Struct

# Test simple packing and unpacking

import struct
import _struct

def testPack(format, expected, value):
    result = _struct.pack(format, value)
