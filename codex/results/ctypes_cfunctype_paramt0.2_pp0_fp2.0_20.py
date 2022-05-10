import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a+b

myfunc = FUNTYPE(myfunc)

print myfunc(1, 2)
</code>

