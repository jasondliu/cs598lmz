import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(a, b):
    return a + b

f.restype = ctypes.c_int
f.argtypes = [ctypes.c_int, ctypes.c_int]

f_cfunc = FUNTYPE(f)

f_cfunc(1, 2)

# 3
</code>

