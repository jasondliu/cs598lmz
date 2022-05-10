import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_setattr():
    s = S()
    s.x = 42
    assert s.x == 42
    raises(TypeError, "s.x = 'hello'")
    raises(TypeError, "s.x = None")
    raises(TypeError, "s.x = s")
    raises(TypeError, "s.x = s.x")
    raises(TypeError, "s.x = ctypes.c_int(42)")
    raises(TypeError, "s.x = ctypes.c_int")
    raises(TypeError, "s.x = ctypes.c_int()")

def test_cfield_getattr():
    s = S()
    assert type(s.x) is ctypes.c_int
    assert s.x == 0

def test_cfield_delattr():
    s = S()
    raises(TypeError, "del s.x")

def test_cfield_repr():
    assert repr(S.x) == "<field 'x' of 'S' objects
