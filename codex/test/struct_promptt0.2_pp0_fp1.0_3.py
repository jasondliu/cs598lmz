import _struct
# Test _struct.Struct.format

import struct

def test(fmt, expected):
    s = _struct.Struct(fmt)
