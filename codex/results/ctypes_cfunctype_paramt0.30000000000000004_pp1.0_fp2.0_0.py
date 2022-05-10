import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_func(a, b):
    print "my_func(%d, %d) called" % (a, b)
    return a + b

f = FUNTYPE(my_func)
print f(1, 2)
</code>

