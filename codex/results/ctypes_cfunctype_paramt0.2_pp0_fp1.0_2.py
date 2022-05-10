import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print "func(%d)" % x
    return x

f = FUNTYPE(func)
f(42)
</code>

