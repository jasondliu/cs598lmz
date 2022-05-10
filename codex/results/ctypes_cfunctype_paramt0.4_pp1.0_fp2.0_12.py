import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x + 1

cfunc = FUNTYPE(myfunc)
print cfunc(1)
</code>
This will print 2.

