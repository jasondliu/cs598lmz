import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print(a, b)
    return a + b

cfunc = FUNTYPE(myfunc)
print(cfunc(1, 2))
</code>

