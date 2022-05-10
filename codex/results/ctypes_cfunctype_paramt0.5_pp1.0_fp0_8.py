import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(x, y):
    return x + y

f_c = FUNTYPE(f)
f_c(1, 2)
</code>

