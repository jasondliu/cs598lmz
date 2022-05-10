import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

# Convert the Python callback into C callback
cb = FUNTYPE(my_callback)

# Call the C function, which will in turn call the Python callback
lib.my_function(1, 2, cb)
</code>

