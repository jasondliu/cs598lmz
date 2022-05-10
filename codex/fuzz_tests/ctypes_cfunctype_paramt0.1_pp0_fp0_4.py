import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    return x + 1

cfunc = FUNTYPE(func)

print(cfunc(1))
</code>

