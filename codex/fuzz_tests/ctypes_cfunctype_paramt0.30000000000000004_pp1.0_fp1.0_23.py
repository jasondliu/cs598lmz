import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def c_callback(a, b):
    print(a, b)
    return a + b

# Convert the Python callback into C callback
c_callback = FUNTYPE(c_callback)

# Call C function
lib.c_function(c_callback)
</code>

