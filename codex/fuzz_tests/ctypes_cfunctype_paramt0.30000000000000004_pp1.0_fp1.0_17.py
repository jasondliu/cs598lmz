import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def f(x):
    return x+1

cfunc = FUNTYPE(f)
print cfunc(2)
</code>

