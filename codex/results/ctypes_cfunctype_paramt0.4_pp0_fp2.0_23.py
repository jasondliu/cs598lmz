import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(n):
    print "func(%d)" % n
    return n + 1

cfunc = FUNTYPE(func)
cfunc(1)
</code>

