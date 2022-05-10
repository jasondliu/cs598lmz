import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42
    assert type(s.x) is ctypes.c_int
    assert type(s.x) is ctypes.CField
    raises(AttributeError, "s.x = 'abc'")
    raises(AttributeError, "s.x = 1.23")
    raises(AttributeError, "s.x = S()")
    raises(AttributeError, "s.x = None")
    raises(AttributeError, "s.x = s")
    raises(AttributeError, "s.x = [1,2,3]")
    raises(AttributeError, "s.x = (1,2,3)")
    raises(AttributeError, "s.x = {'abc': 42}")
    raises(AttributeError, "s.x = object()")
    raises(AttributeError, "s.x = object")
    raises(AttributeError, "s.x = type")
    raises(AttributeError, "s.
