import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_int, ctypes.c_int)

# Create a function object for the callback
def my_callback(a, b):
    return a + b

CALLBACK = FUNTYPE(my_callback)

# Call the C function and pass the function object as an argument
lib.do_something(CALLBACK)
</code>

