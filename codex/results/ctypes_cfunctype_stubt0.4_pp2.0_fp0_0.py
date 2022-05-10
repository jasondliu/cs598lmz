import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
# ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(ctypes.c_int))

# ctypes.POINTER(ctypes.c_int)
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes.POINTER(ctypes.c_int)()
# ctypes
