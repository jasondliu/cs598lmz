import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

cfunc = FUNTYPE(func)

print cfunc(2)
