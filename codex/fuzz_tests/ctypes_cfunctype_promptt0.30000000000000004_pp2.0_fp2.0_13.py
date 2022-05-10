import ctypes
# Test ctypes.CFUNCTYPE
def test_CFUNCTYPE():
    def func(a, b):
        return a + b
    func_ptr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
    assert func_ptr(1, 2) == 3

# Test ctypes.POINTER
def test_POINTER():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    x = X(1)
    assert x.a == 1
    x_ptr = ctypes.POINTER(X)(x)
    assert x_ptr.contents.a == 1
    x_ptr.contents.a = 2
    assert x.a == 2

# Test ctypes.byref
def test_byref():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
    x = X(1)
    assert x.a == 1
    x_ptr = ctypes.by
