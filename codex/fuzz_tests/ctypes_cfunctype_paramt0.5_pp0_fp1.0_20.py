import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def f(x, y):
    return x + y

cfun = FUNTYPE(f)
print(cfun(1, 2))
</code>

