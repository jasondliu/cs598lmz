import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_unary():
    assert -1 == -1
    assert type(1) == type(1)
    assert type(1) != type(1.0)
    assert not 1 == 0
    assert 1 != 0
    assert not bool(0)
    assert bool(1)
    assert False is False
    assert not False
    assert True is True
    assert True
    assert type(-1) is int
    assert type(-1.0) is float
    assert type(-1j) is complex
    assert type(-1) is not type(-1.0)
    assert type(-1) is not type(-1j)

def test_float():
    import math
    assert isinstance(1.5, float)
    assert isinstance(1.5, int) is False
    assert 1.5 == 1.5
    assert 1.5 != 1.6
    assert 1.5 < 1.6
    assert 1.6 > 1.5
    assert 1.6 >= 1.5
    assert 1.5 <= 1.6
    assert round(0.5
