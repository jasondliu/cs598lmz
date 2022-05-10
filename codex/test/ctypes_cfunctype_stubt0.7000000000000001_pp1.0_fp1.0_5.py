import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 12345
ctypes.cast(fun, ctypes.c_void_p).value
