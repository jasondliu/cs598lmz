import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_get_field_type():
    assert ctypes.CField.__getitem__(S.x, 0) is ctypes.c_int

def test_get_field_name():
    assert ctypes.CField.__getitem__(S.x, 'x') is ctypes.c_int

def test_get_field_name_failure():
    raises(IndexError, ctypes.CField.__getitem__, S.x, 'y')
