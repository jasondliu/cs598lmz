import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

def test_basic_field():
    s = S(7)
    assert s.x == 7
    assert type(s.x) is ctypes.c_int
    s.x = 8
    assert s.x == 8
    py.test.raises(TypeError, "s.x = 'foo'")
    py.test.raises(TypeError, "s.x = 'foo'")

def test_basic_field_attr():
    s = S(7)
    assert s.x == 7
    assert type(s.x) is ctypes.c_int
    s.x = 8
    assert s.x == 8
    py.test.raises(TypeError, "s.x = 'foo'")
    py.test.raises(TypeError, "s.x = 'foo'")

def test_basic_field_arg():
    s = S(7)
    assert s.x == 7
    assert type(
