import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback!"
    return a + b

c_callback = FUNTYPE(my_callback)

lib.set_callback(c_callback)

print lib.use_callback(1, 2)
</code>

