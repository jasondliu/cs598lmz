import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

def test_setattr():
    s = S()
    s.x = 42
    assert s.x == 42
    raises(AttributeError, "s.y = 42")
    raises(AttributeError, "s.z = 42")
    raises(TypeError, "s.x = 'hello'")

    c = C()
    c.x = 42
    assert c.x == 42
    c.y = 43
    assert c.y == 43
    raises(AttributeError, "c.z = 42")
    raises(TypeError, "c.x = 'hello'")

def test_getattr():
    s = S()
    s.x = 42
    assert s.x == 42
    raises(AttributeError, "s.y")
    raises(AttributeError, "s.z")

    c = C()
    c.x = 42
    assert c.x == 42
    c.
