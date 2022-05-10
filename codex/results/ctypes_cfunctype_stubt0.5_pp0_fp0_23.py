import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

py_object_p = ctypes.POINTER(ctypes.py_object)

def test_call_py_object_p(lib):
    lib.fun.argtypes = [py_object_p]
    lib.fun.restype = None
    lib.fun(fun())

def test_call_py_object_p_byref(lib):
    lib.fun.argtypes = [ctypes.byref(py_object_p)]
    lib.fun.restype = None
    lib.fun(fun())

def test_call_py_object_p_byref_byval(lib):
    lib.fun.argtypes = [ctypes.byref(py_object_p)]
    lib.fun.restype = None
    lib.fun(ctypes.byref(fun()))
