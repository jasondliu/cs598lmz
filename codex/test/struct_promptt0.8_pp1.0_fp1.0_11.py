import _struct
# Test _struct.Struct

def check(t, v, p):
    s = _struct.Struct(t)
    got = s.pack(*v)
