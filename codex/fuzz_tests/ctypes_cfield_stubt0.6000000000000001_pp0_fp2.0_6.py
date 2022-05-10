import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_type_compare():
    assert ctypes.type(ctypes.c_int) == ctypes.c_int
    assert ctypes.type(ctypes.c_int) != ctypes.c_short
    assert ctypes.type(ctypes.c_int) != 42

def test_type_repr():
    assert repr(ctypes.c_int) == "<class 'c_int'>"
    assert repr(ctypes.c_int).startswith("<class 'c_int'")

def test_type_str():
    assert str(ctypes.c_int) == "<class 'c_int'>"
    assert str(ctypes.c_int).startswith("<class 'c_int'")

def test_type_from_param():
    assert ctypes.c_int._type_ == ctypes.c_int
    assert ctypes.c_int._type_() == ctypes.c_int

def test_field_type():
    assert ctypes.type(S.x) == ctypes.
