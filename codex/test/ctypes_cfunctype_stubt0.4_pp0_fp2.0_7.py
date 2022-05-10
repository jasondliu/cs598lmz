import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_ctypes():
    f = fun()
    assert f() is None

def test_ctypes_with_arg():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    @FUNTYPE
    def fun(x):
        return x
    f = fun(42)
    assert f() == 42
