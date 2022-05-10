import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()

print(ctypes.cast(fun, ctypes.c_void_p).value)
