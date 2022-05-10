import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    s = S()
    s.x = 42
    assert s.x == 42
    assert type(s.x) is ctypes.c_int
    assert type(S.x) is ctypes.CField
    assert type(s.x) is type(S.x)
    assert repr(s.x) == '<CField \'x\' of \'S\' objects>'
    assert repr(S.x) == '<CField \'x\' of \'S\' objects>'
    assert str(s.x) == 'x'
    assert str(S.x) == 'x'

test()
