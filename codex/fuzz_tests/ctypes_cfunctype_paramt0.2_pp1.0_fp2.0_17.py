import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(arg1, arg2):
    print "my_callback called with %d, %d" % (arg1, arg2)
    return 0

my_callback_ctypes = FUNTYPE(my_callback)

my_callback_ctypes(1, 2)
</code>

