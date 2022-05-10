import _struct
# Test _struct.Struct()

import sys

def test_struct(fmt, x):
    s = _struct.Struct(fmt)
    got = s.pack(x)
    expected = struct.pack(fmt, x)
