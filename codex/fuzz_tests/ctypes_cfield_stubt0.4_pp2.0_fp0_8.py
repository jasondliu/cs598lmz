import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField
    assert S.x.__class__ is ctypes.CField
    assert isinstance(S.x, ctypes.CField)

def test_cfield_name():
    assert S.x.name == 'x'
    assert S.x.__name__ == 'x'

def test_cfield_offset():
    assert S.x.offset == 0
    assert S.x.__offset__ == 0

def test_cfield_type():
    assert S.x.ctype is ctypes.c_int
    assert S.x.__ctype__ is ctypes.c_int

def test_cfield_repr():
    assert repr(S.x) == "<CField 'x' of type 'c_int'>"

def test_cfield_str():
    assert str(S.x) == 'x'

def test_cfield_get():
    s = S(42)
    assert s.x == 42
    assert S
