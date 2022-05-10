import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print(a, b)
    return a + b

cfunc = FUNTYPE(func)

print(cfunc(1, 2))
</code>

