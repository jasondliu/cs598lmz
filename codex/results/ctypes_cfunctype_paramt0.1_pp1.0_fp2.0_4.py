import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "in python callback", a, b
    return a + b

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)

print lib.call_callback(1, 2)
</code>

