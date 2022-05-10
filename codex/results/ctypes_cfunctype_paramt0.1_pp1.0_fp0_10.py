import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "my_callback called with", x
    return x + 1

my_callback_c = FUNTYPE(my_callback)

lib.my_callback_func(my_callback_c)
</code>

