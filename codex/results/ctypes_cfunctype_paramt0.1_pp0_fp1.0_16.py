import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

cb_func = FUNTYPE(my_callback)

lib.register_callback(cb_func)
lib.call_registered_callback(1, 2)
</code>

