import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    print "hello", x
    return x

f = FUNTYPE(myfunc)
f(42)
</code>

