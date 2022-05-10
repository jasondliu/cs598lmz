import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    def func(a, b):
        return a + b
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)
    assert cfunc(1, 2) == 3
    assert cfunc.__name__ == 'func'
    assert cfunc.__module__ == '__main__'
    assert cfunc.__doc__ == None
    assert cfunc.__dict__ == {}

# Test ctypes.Structure
def test_structure():
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    x = X()
    assert x.a == 0
    assert x.b == 0
    x.a = 1
    x.b = 2
    assert x.a == 1
    assert x.b == 2

# Test ctypes.Union
def test_union():
    class X(ctypes.Union):
       
