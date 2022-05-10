import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

def test_cfield():
    s = S()
    s.x = 42
    assert isinstance(s.x, ctypes.CField)
    assert s.x == 42
    assert s.x + 1 == 43
    assert s.x - 1 == 41
    assert s.x * 2 == 84
    assert s.x & 1 == 0
    assert s.x | 1 == 43
    assert s.x ^ 1 == 43
    assert s.x << 1 == 84
    assert s.x >> 1 == 21
    assert -s.x == -42
    assert +s.x == 42
    assert abs(s.x) == 42
    assert int(s.x) == 42
    assert float(s.x) == 42.0
    assert hex(s.x) == '0x2a'
    assert oct(s.x) == '052'
    assert bin(s.x) == '0b101010'
    assert ctypes.
