import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_double)

def func(x):
    print(x)

cfunc = FUNTYPE(func)
cfunc(1.0)
</code>

