import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

my_callback_c = FUNTYPE(my_callback)

lib.call_my_callback(my_callback_c)
</code>

