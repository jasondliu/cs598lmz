import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

mycallback = FUNTYPE(myfunc)

lib.myfunc(mycallback)
</code>

