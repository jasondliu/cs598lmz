import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert S.x.__class__ is ctypes.CField
    assert S.x.__name__ == 'x'
    assert S.x.__doc__ == 'c_int'
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.ctype == ctypes.c_int

def test_cfield_get():
    s = S()
    s.x = 42
    assert s.x == 42

def test_cfield_set():
    s = S()
    s.x = 42
    assert s.x == 42

def test_cfield_set_error():
    s = S()
    raises(TypeError, "s.x = 'x'")

def test_cfield_get_error():
    s = S()
    raises(TypeError, "s.x")

class S2(ctypes.Structure):
    _fields_ = [
