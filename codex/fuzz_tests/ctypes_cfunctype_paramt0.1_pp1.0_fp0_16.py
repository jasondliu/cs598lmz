import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

cb = FUNTYPE(my_callback)

lib.my_function(1, cb)
</code>

