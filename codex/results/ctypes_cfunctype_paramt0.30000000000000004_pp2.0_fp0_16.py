import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following is the callback function.
def my_callback(arg):
    print "callback called with arg =", arg
    return 0

# Convert the Python callback into C pointer.
CMPFUNC = FUNTYPE(my_callback)

# Call the C function.
lib.call_func(CMPFUNC)
</code>

