import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert type(S.x) is ctypes.CField
    assert type(S.x) is ctypes.CField

def test_cfield_repr():
    assert repr(S.x) == "<field 'x' of 'S' objects>"
    assert repr(S.x) == "<field 'x' of 'S' objects>"

def test_cfield_get():
    s = S()
    assert S.x.__get__(s) == 0
    assert S.x.__get__(s) == 0

def test_cfield_set():
    s = S()
    S.x.__set__(s, 42)
    assert s.x == 42

def test_cfield_set_wrong_type():
    s = S()
    raises(TypeError, S.x.__set__, s, 42.0)

def test_cfield_set_readonly():
    s = S()
    raises(AttributeError, S.x.__set__, s, 42)

