import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(x):
    print "callback called with", x
    return x + 1

my_callback_c = FUNTYPE(my_callback)

# now pass it to the C function

lib.call_my_callback(my_callback_c)
</code>

