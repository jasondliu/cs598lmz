import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_c_function_type_returns_none():
    assert fun() is None

def test_c_function_type_returns_none_from_python():
    def fun():
        return None
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    fun = FUNTYPE(fun)
    assert fun() is None

def test_c_function_type_returns_none_from_python_with_arg():
    def fun(x):
        return None
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    fun = FUNTYPE(fun)
    assert fun(1) is None

def test_c_function_type_returns_none_from_python_with_arg_and_kwarg():
    def fun(x, y=1):
        return None
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    fun = FUNTYPE(fun)

