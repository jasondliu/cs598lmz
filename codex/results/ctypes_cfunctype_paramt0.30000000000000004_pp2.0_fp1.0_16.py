import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    return a + b

my_callback = FUNTYPE(myfunc)

lib.myfunc(my_callback)
</code>

