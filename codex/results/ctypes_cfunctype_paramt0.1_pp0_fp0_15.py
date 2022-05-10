import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

CALLBACK = FUNTYPE(my_callback)

lib.register_callback(CALLBACK)

lib.call_registered_callback(42)
</code>

