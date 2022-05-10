import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback called with %d and %d" % (a, b)

my_callback_type = FUNTYPE(my_callback)

my_callback_ptr = my_callback_type.__cast(ctypes.c_void_p.in_dll(lib, "my_callback"))

lib.call_my_callback(my_callback_ptr, 1, 2)
</code>

