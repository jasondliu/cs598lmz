import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(i):
    print "callback", i
    return i

my_callback_func = FUNTYPE(my_callback)

my_callback_func(1)
</code>

