import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('z', ctypes.c_int)]

class S4(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

s = S(42)
s2 = S2(42)

def test(lib, body):
    for func, restype, argtypes in [
        (lib.test_S_S, S, (S,)),
        (lib.test_S_S_S, S, (S, S)),
        (lib.test_S_S_S_S, S, (S, S, S)),
        (lib.test_S2_S2, S2, (S2,)),
        (lib.test_S2_S2_S2, S2, (S2, S2)),
        (lib.test_S2_S2_S2_S2, S2,
