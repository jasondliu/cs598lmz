import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print "func(%d)" % x
    return x * x

f = FUNTYPE(func)
print f(5)
</code>

