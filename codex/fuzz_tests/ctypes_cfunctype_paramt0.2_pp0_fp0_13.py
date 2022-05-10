import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python:", a, b
    return a + b

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)

lib.call_from_c(1, 2)
</code>

