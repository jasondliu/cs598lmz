import _struct
# Test _struct.Struct.

def check(fmt, expected, value):
    s = _struct.Struct(fmt)
    got = s.pack(value)
