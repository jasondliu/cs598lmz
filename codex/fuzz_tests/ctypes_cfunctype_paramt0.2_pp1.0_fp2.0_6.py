import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print "my_callback called with", a
    return 0

my_callback_func = FUNTYPE(my_callback)

lib.my_function(my_callback_func)
</code>

