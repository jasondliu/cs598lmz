import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_py_object():
    assert fun() == 1
    raises(ctypes.ArgumentError, FUNTYPE, ctypes.c_int)

def test_py_object_return_None():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    @FUNTYPE
    def fun(x):
        return None
    assert fun(None) is None

def test_py_object_return_None_with_result():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    @FUNTYPE
    def fun(x):
        return None
    assert fun(None) is None
    res = ctypes.py_object()
    fun(None, res)
    assert res.value is None

def test_py_object_return_None_with_result_2():
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
