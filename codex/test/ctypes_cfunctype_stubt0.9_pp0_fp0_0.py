import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert type(fun) is FUNTYPE
fun()

# This is the code that doesn't work...
