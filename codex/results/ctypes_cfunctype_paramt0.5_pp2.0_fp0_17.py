import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y):
    return x + y

# Register the callback function
my_callback_func = FUNTYPE(my_callback)

# Use the callback function in the C library
lib.process_data(my_callback_func)
</code>

