import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python:", a, b
    return a + b

callback = FUNTYPE(my_callback)

lib.call_from_c(5, 6, callback)
</code>

