import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_CField_instance():
    s = S()
    assert isinstance(s.x, ctypes.CField)

def test_CField_set_overflow():
    import _testcapi
    s = S()
    assert s.x == 0
    raises(OverflowError, "s.x = _testcapi.INT_MIN")
    raises(OverflowError, "s.x = _testcapi.INT_MAX + 1")
    assert s.x == 0

def test_CField_get_overflow():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_ubyte)]
    s = S(x=0xffffffff)
    assert s.x == 0xff

def test_CField_set_by_index():
    s = S()
    assert s.x == 0
    s[0] = 42
    assert s.x == 42
    s[0] = -42
    assert s.x == -42

def test_CField_
