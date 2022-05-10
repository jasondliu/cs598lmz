import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

cfunc = FUNTYPE(f)
print cfunc(1, 2)
</code>

