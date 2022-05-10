import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

cb_func = FUNTYPE(my_callback)

lib.my_function(5, cb_func)
</code>

