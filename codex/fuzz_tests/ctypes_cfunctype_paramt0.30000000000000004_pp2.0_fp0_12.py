import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with", x)
    return x

cb = FUNTYPE(my_callback)

lib.my_function(5, cb)
</code>

