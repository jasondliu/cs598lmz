import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def my_callback(a):
    print "callback called with", a
    return 0

my_callback_wrapper = FUNTYPE(my_callback)

my_callback_wrapper(42)
</code>

