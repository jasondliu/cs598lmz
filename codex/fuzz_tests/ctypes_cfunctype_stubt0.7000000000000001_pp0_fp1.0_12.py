import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = ctypes.c_int()
    x.value = 3
    return x
</code>

