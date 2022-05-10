import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.Array = type(S._fields_)

def test_primitive_field_get_set():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42

def test_primitive_field_repr():
    f = S.x
    assert repr(f) == "<CField 'x' of 'S'>"

def test_structure_array():
    s = S()
    assert s.x == 0
    s.x = 42
    assert s.x == 42
