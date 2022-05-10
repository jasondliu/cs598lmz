import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def myfunc(a, b):
    print "myfunc(%d, %d) called" % (a, b)
    return a + b

f = FUNTYPE(myfunc)
print f(1, 2)
</code>

