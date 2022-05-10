import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

cb_fun = FUNTYPE(my_callback)

# Now "some_c_function" is a Python function that will call the
# callback.
some_c_function(cb_fun)
</code>

