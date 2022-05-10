import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "callback called with", x
    return x

my_callback_c = FUNTYPE(my_callback)

lib.register_callback(my_callback_c)
lib.call_registered_callback(10)
</code>

