import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_call_with_pyobj():
    assert fun() is None
    raises(TypeError, fun, 42)

def test_call_with_pyobj_raise():
    def f():
        raise ValueError
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def g():
        return f()
    raises(ValueError, g)

def test_call_with_pyobj_null():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def g():
        return ctypes.py_object(None)
    assert g() is None

def test_call_with_pyobj_null_raise():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    @FUNTYPE
    def g():
        return ctypes.py_object(None)
    raises(TypeError, g, 42)

