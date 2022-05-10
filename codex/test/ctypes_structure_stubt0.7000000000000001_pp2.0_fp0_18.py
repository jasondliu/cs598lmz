import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

def f(x):
    return x

def test_wrap_function():
    test_wrap_function.lib.f.restype = ctypes.POINTER(S)
    test_wrap_function.lib.f.argtypes = [ctypes.POINTER(S)]
    s = S()
    assert f(s) is f(s)


def test_wrap_method():
    test_wrap_method.lib.S_f.restype = ctypes.POINTER(S)
    test_wrap_method.lib.S_f.argtypes = [ctypes.POINTER(S)]
    s = S()
    assert s.f() is s.f()

def test_wrap_class():
    assert test_wrap_class.lib.S()

def test_wrap_void_result():
    test_wrap_void_result.lib.f.restype = None
    test_wrap_void_result.lib.f.argtypes = [ctypes.c_int]
    assert test_wrap_
