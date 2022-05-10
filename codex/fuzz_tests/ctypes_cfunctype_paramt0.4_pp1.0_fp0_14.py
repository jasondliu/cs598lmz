import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback({}, {})".format(a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

# This will print "my_callback(1, 2)".
my_callback_c(1, 2)
</code>

