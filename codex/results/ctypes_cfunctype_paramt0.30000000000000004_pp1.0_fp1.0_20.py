import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def pyfunc(x):
    return x + 1

cfunc = FUNTYPE(pyfunc)

print(cfunc(1))
</code>

