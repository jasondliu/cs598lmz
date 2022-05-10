import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_get_set():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is int
    assert type(S.x) is ctypes.CField

def test_cfield_get_set_with_instance():
    s = S()
    s.x = 42
    assert S.x.__get__(s) == 42
    assert type(S.x.__get__(s)) is int
    S.x.__set__(s, 100)
    assert s.x == 100
    assert type(s.x) is int

def test_cfield_get_set_with_class():
    assert S.x.__get__(S) is S.x
    assert type(S.x.__get__(S)) is ctypes.CField
    S.x.__set__(S, 100)
    assert S.x == 100
    assert type(S.x) is int

def test_cfield_get_set_with_none
