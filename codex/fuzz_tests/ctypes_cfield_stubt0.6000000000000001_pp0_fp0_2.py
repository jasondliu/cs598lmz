import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_basic():
    s = S()
    def set_x(val):
        s.x = val
    assert raises(ValueError, set_x, 1.0)
    assert raises(ValueError, set_x, "hello")
    assert raises(ValueError, set_x, None)
    assert raises(OverflowError, set_x, 2**100)
    assert raises(OverflowError, set_x, -2**100)
    s.x = 123
    assert s.x == 123
    assert type(s.x) is int
    s.x = 42
    assert s.x == 42
    assert type(s.x) is int
    s.x = -42
    assert s.x == -42
    assert type(s.x) is int
    s.x = 0
    assert s.x == 0
    assert type(s.x) is int
    def del_x():
        del s.x
    assert raises(AttributeError, del_x)

def test_address():
    s = S()
   
