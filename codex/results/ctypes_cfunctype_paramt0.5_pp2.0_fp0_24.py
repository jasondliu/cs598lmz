import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def my_callback(x,y):
    print("my_callback called with %d, %d" % (x, y))
    return 0

my_callback_type = FUNTYPE(my_callback)

my_callback_ptr = ctypes.cast(my_callback_type, ctypes.c_void_p).value

# Now, the tricky part:
# In the C code, we need to call the callback and pass it the pointer to the callback function.
# We cannot just pass the pointer, as it is a Python integer, and the C code will not know what to do with it.
# Instead, we pass an int array of length 1, and store the pointer in the first (and only) element of the array.
# The C code then accesses this array and extracts the pointer, which can then be used to call back into Python.

# Here's how to call the C code and pass our callback, together with the pointer to the callback function:

# Create an int array of length 1
intArray
