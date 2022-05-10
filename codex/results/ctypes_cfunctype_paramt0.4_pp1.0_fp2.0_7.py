import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def f(x):
    return x**2

cfunc = FUNTYPE(f)

print(cfunc(2.0))
</code>

