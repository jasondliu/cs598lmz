import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x*x

cfunc = FUNTYPE(func)

print cfunc(2)
</code>

