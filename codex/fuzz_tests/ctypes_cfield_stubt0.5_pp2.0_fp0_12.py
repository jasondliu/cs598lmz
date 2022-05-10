import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def test():
    s = S(42)
    s2 = S2(s.x)
    assert s2.x == 42
    s2.x = 24
    assert s2.x == 24
    s2.x = S3(42).x
    assert s2.x == 42

test()
