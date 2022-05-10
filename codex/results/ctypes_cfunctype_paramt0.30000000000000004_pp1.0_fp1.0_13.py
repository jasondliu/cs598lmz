import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print("callback called with {}".format(x))
    return 0

my_callback_c = FUNTYPE(my_callback)

lib.my_function(my_callback_c)
</code>

