import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print x
    return x

# Create the callback.
CALLBACK = FUNTYPE(callback)

# Create the C function.
lib.my_function.argtypes = (ctypes.c_int, FUNTYPE)
lib.my_function.restype = ctypes.c_int

# Call the C function.
lib.my_function(1, CALLBACK)
</code>

