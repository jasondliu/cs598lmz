import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32
    _fields_ = [('x', ctypes.c_uint32),
                ('y', ctypes.c_uint32)]

def _test(x, y, use_fields=True):
    if use_fields:
        s = S()
        s.x = x
        s.y = y
        z = s.x + s.y
        return z

def test(use_fields):
    print "use_fields=", use_fields
    _test(1, 2, use_fields=use_fields)
    res = interpret(test, [use_fields])
    assert res == 3
    assert _test(1, 2, use_fields=use_fields) == 3

def test_len():
    s = S()
    s.x = 1
    s.y = 2
    assert len(s) == 2

def test_field_names():
    assert S._fields_ == [('x', ctypes.c_uint32),
                          ('y',
