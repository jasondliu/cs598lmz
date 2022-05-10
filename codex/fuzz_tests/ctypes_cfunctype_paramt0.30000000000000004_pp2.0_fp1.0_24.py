import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(2, 3))
</code>

