import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

def test_call_into_py():
    assert fun() == 3

def test_call_py_function_from_c():
    import ctypes
    dll = ctypes.CDLL(str(py.path.local(__file__).join('cfuncs.so')))
    f = dll.call_py_function
    f.argtypes = [ctypes.py_object]
    f.restype = ctypes.c_int
    res = f(fun)
    assert res == 3

def test_call_py_function_from_c_via_callback():
    import ctypes
    dll = ctypes.CDLL(str(py.path.local(__file__).join('cfuncs.so')))
    f = dll.call_py_function_via_callback
    f.argtypes = [ctypes.py_object]
    f.restype = ctypes.c_int
    res = f(fun)
    assert res == 3

