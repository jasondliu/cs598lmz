import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    return n * 2

cfunc = FUNTYPE(func)

print cfunc(2)
</code>

