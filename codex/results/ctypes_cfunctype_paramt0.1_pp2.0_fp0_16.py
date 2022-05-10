import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("my_callback called with %d" % x)
    return x

my_callback_c = FUNTYPE(my_callback)

lib.my_function(my_callback_c)
</code>

