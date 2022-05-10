import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(arg):
    print("callback called with arg %d" % arg)
    return 0

CALLBACK = FUNTYPE(my_callback)

lib.set_callback(CALLBACK)

lib.call_callback(0)
</code>

