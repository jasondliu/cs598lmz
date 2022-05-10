import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

CMPFUN = FUNTYPE(f)

print(CMPFUN(1, 2))
</code>

