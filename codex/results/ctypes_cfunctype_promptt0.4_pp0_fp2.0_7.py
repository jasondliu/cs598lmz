import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunctype():
    class X(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]
    def func(x):
        return x.x
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, X)(func)
    assert cfunc(X(42)) == 42
    assert cfunc.__name__ == 'func'
    assert cfunc.__doc__ == func.__doc__

def test_cfunctype_doc():
    def func(x):
        """hello"""
        return x
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
    assert cfunc.__doc__ == "hello"

def test_cfunctype_doc_none():
    def func(x):
        return x
    func.__doc__ = None
    cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(func)
    assert cfunc
