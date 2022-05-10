import _struct
# Test _struct.Struct()

import _struct

def test(fmt, input, output):
    s = _struct.Struct(fmt)
    got = s.unpack(s.pack(*input))
