import ctypes
# Test ctypes.CFUNCTYPE
def myfunc(a, b):
    return a + b
myfunc = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)(myfunc)
