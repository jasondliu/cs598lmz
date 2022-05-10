import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(x):
    print "func", x
    return x * 2

f = FUNTYPE(func)
print f(4)
</code>

