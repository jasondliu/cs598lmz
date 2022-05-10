import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
def cfunc(f):
    return FUNTYPE(f)
</code>

