import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback_type = FUNTYPE(my_callback)

my_callback_func = my_callback_type(my_callback)

print my_callback_func(1, 2)
</code>

