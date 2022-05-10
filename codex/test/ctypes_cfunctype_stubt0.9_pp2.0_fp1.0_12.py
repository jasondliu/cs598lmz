import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

assert(fun() == 3)

@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 3

assert(fun() == 3)
 
