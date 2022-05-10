import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback is called with %d and %d" % (a, b))
    return a + b

cb_func = FUNTYPE(my_callback)

# Now we can pass the callback to the C library.
lib.process(cb_func)
</code>

