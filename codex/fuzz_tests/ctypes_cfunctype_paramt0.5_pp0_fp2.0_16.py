import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def myfunc(x):
    return x**2

cfunc = FUNTYPE(myfunc)

print "calling python function"
print myfunc(2)
print "calling c function"
print cfunc(2)
</code>

