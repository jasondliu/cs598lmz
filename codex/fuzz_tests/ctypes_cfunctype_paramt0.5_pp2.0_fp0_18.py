import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(n):
    return n*2

myfunc_c = FUNTYPE(myfunc)

print(myfunc_c(5))
</code>

