import _struct
# Test _struct.Struct.

def test(fmt, *args):
    s = _struct.Struct(fmt)
