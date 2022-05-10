import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(x, y):
    return x * y

cfunc = FUNTYPE(myfunc)

print cfunc(2, 3)
# 6
</code>

