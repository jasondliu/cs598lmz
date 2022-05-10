import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_py_callable():
    assert isinstance(fun, ctypes.PyCallable)
    assert isinstance(fun, ctypes.CFUNCTYPE)

