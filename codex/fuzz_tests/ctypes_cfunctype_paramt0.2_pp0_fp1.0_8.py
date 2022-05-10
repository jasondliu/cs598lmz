import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback = FUNTYPE(my_callback)

lib.set_callback(my_callback)

print lib.call_callback(1, 2)
</code>

