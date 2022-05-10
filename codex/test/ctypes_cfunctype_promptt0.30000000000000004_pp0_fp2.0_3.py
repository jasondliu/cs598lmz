import ctypes
# Test ctypes.CFUNCTYPE

def test_CFUNCTYPE():
    from ctypes import CFUNCTYPE, c_int
    f = CFUNCTYPE(c_int, c_int, c_int)(lambda a, b: a + b)
    assert f(1, 2) == 3
    assert f.argtypes == (c_int, c_int)
    assert f.restype == c_int

def test_CFUNCTYPE_errcheck():
    from ctypes import CFUNCTYPE, c_int
    def errcheck(result, func, args):
        return args[0]
    f = CFUNCTYPE(c_int, c_int, c_int, errcheck=errcheck)(lambda a, b: a + b)
    assert f(1, 2) == 1

def test_CFUNCTYPE_with_defaults():
    from ctypes import CFUNCTYPE, c_int
