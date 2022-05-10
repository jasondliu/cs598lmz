import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_hash():
    s = S()
    s.x = 10

    d = {}
    d[s] = 1

    assert d[s] == 1
    s.x = 20
    assert d[s] == 1

    d[s] = 2
    assert d[s] == 2

    s.x = 30
    assert d[s] == 2
