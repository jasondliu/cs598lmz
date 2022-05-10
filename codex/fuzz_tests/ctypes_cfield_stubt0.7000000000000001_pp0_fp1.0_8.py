import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert issubclass(S.x.__class__, ctypes.CField)

def test_setattr():
    assert S.x.__get__(S()) == 0
    S.x.__set__(S(), 1)
    assert S.x.__get__(S()) == 1

def test_setattr_noconv():
    S_ = ctypes.Structure
    class S(S_):
        _fields_ = [('x', ctypes.c_int)]
    S.x.__set__(S(), 1, False)
    assert S.x.__get__(S()) == 1

def test_noconv():
    try:
        S.x.__set__(S(), "x")
    except TypeError:
        pass
    else:
        assert 0, "should have raised TypeError"

    try:
        S.x = "x"
    except TypeError:
        pass
    else:
        assert 0, "should have raised TypeError"

def test_
