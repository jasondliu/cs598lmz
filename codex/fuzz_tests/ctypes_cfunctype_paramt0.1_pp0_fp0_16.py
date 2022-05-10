import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with %d" % x)
    return 0

my_callback_func = FUNTYPE(my_callback)

lib.my_function.argtypes = [FUNTYPE]
lib.my_function(my_callback_func)
</code>

