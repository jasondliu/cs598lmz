import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

f = FUNTYPE(myfunc)
print f(1)
</code>

