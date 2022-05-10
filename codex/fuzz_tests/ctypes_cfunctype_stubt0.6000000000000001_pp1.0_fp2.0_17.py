import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

def test_fun(lib):
    lib.test_fun.argtypes = [FUNTYPE]
    lib.test_fun.restype = ctypes.c_uint
    assert lib.test_fun(fun) == 0

def test_fun_null(lib):
    lib.test_fun_null.argtypes = [FUNTYPE]
    lib.test_fun_null.restype = ctypes.c_uint
    assert lib.test_fun_null(None) == 0

def test_fun_call(lib):
    lib.test_fun_call.argtypes = [FUNTYPE]
    lib.test_fun_call.restype = ctypes.c_uint
    assert lib.test_fun_call(fun) == 0


# Test passing a Python function with a callback
def test_fun_callback(lib):
    lib.test_fun_callback.argtypes = [FUNTYPE]
    lib.test_fun_callback.restype = ctypes.c_uint
    def fun():
        pass
    assert lib.test_fun_callback
