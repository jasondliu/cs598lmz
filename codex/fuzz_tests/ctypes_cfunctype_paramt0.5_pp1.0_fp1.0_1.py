import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def my_callback(x):
    # x is a ctypes.c_double
    return x

my_callback_c = FUNTYPE(my_callback)
</code>

