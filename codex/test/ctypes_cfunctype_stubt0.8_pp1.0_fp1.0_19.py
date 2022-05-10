import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 12
fun()

@FUNTYPE
def fun():
    return 1
fun()

# can't assign new type to the same name
@ctypes.CFUNCTYPE(ctypes.c_int)
def fun():
    return 12
fun()
