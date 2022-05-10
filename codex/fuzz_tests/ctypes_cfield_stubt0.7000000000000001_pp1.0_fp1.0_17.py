import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_constructor():
    assert ctypes.CField(S, 'x') is getattr(S, 'x')

def test_name():
    f = ctypes.CField(S, 'x')
    assert f.name == 'x'

def test_ctype():
    f = ctypes.CField(S, 'x')
    assert f.ctype is ctypes.c_int

def test_offset():
    f = ctypes.CField(S, 'x')
    assert f.offset == 0

def test_from_address():
    f = ctypes.CField.from_address(id(S.x), ctypes.c_int)
    assert f.name == 'x'
    assert f.ctype is ctypes.c_int
    assert f.offset == 0

def test_from_address_bad_address():
    raises(ValueError, ctypes.CField.from_address, id(S) + 1, ctypes.c_int)

def test_from_address_bad_type():
