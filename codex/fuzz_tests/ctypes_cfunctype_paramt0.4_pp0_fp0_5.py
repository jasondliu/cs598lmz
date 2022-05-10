import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(a):
    return a*2

cfunc = FUNTYPE(func)

print cfunc(2)
</code>

