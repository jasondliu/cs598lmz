import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with {}".format(x))
    return 0

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)

lib.call_callback(1)
</code>

