import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun(lib):
    lib.test_fun.argtypes = (FUNTYPE,)
    lib.test_fun.restype = ctypes.py_object
    assert lib.test_fun(fun) == 1

def test_fun_null(lib):
    lib.test_fun_null.argtypes = (FUNTYPE,)
    lib.test_fun_null.restype = ctypes.py_object
    assert lib.test_fun_null(None) == 1

def test_fun_null_return(lib):
    lib.test_fun_null_return.argtypes = (FUNTYPE,)
    lib.test_fun_null_return.restype = ctypes.py_object
    assert lib.test_fun_null_return(fun) is None

def test_fun_null_arg_null_return(lib):
    lib.test_fun_null_arg_null_return.argtypes = (FUNTYPE,)
    lib.test_fun_null_arg_null_return.restype = ctypes.py_object

