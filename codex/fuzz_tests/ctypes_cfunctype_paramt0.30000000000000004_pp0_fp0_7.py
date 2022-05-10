import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback = FUNTYPE(my_callback)

# Callback type is now FUNTYPE, and the actual callback is
# wrapped in the my_callback object.

lib.set_callback(my_callback)

# Now call the function in the shared library
lib.call_callback(1, 2)
</code>

