import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(x=S.x):
    print(x.__class__, type(S.x))
    assert x.__class__ is type(S.x)

test()
