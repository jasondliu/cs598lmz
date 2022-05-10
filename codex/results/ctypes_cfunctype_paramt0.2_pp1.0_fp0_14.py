import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback was called with %d and %d" % (a, b))
    return a + b

cb_func = FUNTYPE(my_callback)

# Now "some_lib.some_func" takes a callback function as an argument
some_lib.some_func(cb_func)
</code>

