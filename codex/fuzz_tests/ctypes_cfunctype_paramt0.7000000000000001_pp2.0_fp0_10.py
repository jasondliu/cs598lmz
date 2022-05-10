import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def cb(a, b):
    print "Called with", a, b
    return a + b

print "Result", add_callback(cb, 2, 3)
</code>

