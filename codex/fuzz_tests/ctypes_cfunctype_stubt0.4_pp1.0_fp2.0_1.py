import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

fun()

# ctypes.CFUNCTYPE(return type, *args)
# ctypes.py_object
# ctypes.c_int
