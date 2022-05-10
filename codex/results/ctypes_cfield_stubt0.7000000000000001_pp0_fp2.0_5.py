import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_repr():
    ctypes.CField(ctypes.c_int)
    ctypes.CField(ctypes.c_int, 'x')
    ctypes.CField(ctypes.c_int, 'x', 10)

def test_equality():
    assert S.x == ctypes.CField(ctypes.c_int, 'x', 0)

def test_hash():
    assert hash(S.x) == hash(ctypes.CField(ctypes.c_int, 'x', 0))

def test_init_failures():
    raises(ValueError, ctypes.CField, ctypes.c_int, 'x', 'abc')

def test_invalid_field_name():
    raises(ValueError, ctypes.CField, ctypes.c_int, '1x', 0)

def test_invalid_name_type():
    raises(TypeError, ctypes.CField, ctypes.c_int, 1, 0)

def test_invalid_offset_type():
    raises
