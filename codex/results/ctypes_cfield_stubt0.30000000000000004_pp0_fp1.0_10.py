import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_c_field_setter():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is int

def test_c_field_setter_typeerror():
    s = S()
    raises(TypeError, "s.x = 'hello'")

def test_c_field_setter_overflowerror():
    s = S()
    raises(OverflowError, "s.x = sys.maxint + 1")

def test_c_field_getter():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is int

def test_c_field_getter_typeerror():
    s = S()
    s.x = 42
    raises(TypeError, "s.x + 'hello'")

def test_c_field_getter_overflowerror():
    s = S()
    s.x = sys.maxint
    raises(OverflowError, "s.x
