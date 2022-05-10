import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_py_object():
    assert fun() is None

def test_bool():
    # this is a special case, ctypes.c_bool is a subclass of
    # ctypes.c_int, but we need to check that it is handled
    # separately
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_bool)
    @FUNTYPE
    def fun():
        return True
    assert fun() is True

def test_c_bool_as_int():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
    @FUNTYPE
    def fun():
        return True
    assert fun() == 1

def test_struct_as_return():
    class S(ctypes.Structure):
        _fields_ = [('x', ctypes.c_int)]
    FUNTYPE = ctypes.CFUNCTYPE(S)
    @FUNTYPE
    def fun():
        return S(42)
    assert fun().x == 42

