import _struct
# Test _struct.Struct

def check(t, v, p):
    s = _struct.Struct(t)
    got = s.pack(*v)
    if p != got:
        print t, v, p, got
        raise ValueError
    got = s.unpack(p)
    if v != got:
        print t, v, p, got
        raise ValueError
    size = s.size
    if len(p) != size:
        print t, v, p, got, size
        raise ValueError

def test_byteorder():
    check('=b', (127,), b'\x7f')
    check('=b', (-127,), b'\x81')
    check('=b', (-128,), b'\x80')
    check('<b', (127,), b'\x7f')
    check('<b', (-127,), b'\xff')
    check('<b', (-128,), b'\x80')
    check('>b', (127,), b'\x7f')
    check('>b
