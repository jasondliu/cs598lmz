import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

myfunc_c = FUNTYPE(myfunc)

print myfunc_c(5)
</code>

