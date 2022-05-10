import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def callback(x):
    print "callback called with %d" % x
    return x + 1

# create a C function
cfunc = FUNTYPE(callback)

# create a C function pointer
cptr = ctypes.cast(cfunc, ctypes.c_void_p)

# create a Python wrapper
pfunc = ctypes.pythonapi.PyCObject_AsVoidPtr(cptr)

# call it
print pfunc(1)
</code>

