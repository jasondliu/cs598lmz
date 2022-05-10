import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, rhs):
        return self.x == rhs.x

def test_field():
    s = S(x=1)
    assert s.x == 1

    s.x = 2
    assert s.x == 2

    # test inheritance
    class T(S):
        _fields_ = [('y', ctypes.c_int)]

    t = T(x=3, y=4)
    assert t.x == 3
    assert t.y == 4
    assert type(t.x) is ctypes.c_int
    assert type(t.y) is ctypes.c_int

    t.x = 5
    t.y = 6
    assert t.x == 5
    assert t.y == 6

def test_field_invalid():
    s = S(x=1)
    raises(TypeError, "s.y = 2")
    raises(AttributeError, "s.y")
