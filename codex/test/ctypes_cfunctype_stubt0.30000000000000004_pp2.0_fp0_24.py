import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

# This function is not callable
fun()

# This function is callable
fun.__call__()
