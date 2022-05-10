import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def get_f():
    return FUNTYPE(lambda x,y: x+y)
</code>

