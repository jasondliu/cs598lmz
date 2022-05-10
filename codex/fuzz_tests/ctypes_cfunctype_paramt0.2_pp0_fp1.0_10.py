import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print "my_callback was called with %d and %d" % (a, b)
    return a + b

my_callback_type = FUNTYPE(my_callback)

# Create a C function pointer from the Python callback
my_callback_ptr = my_callback_type(my_callback)

# Pass the function pointer to a C function
lib.call_my_callback(my_callback_ptr, 1, 2)
</code>

