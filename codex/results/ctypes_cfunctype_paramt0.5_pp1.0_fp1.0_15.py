import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_c_callback(a, b):
    """
    This is a Python function that will be passed
    as a callback to the C function.
    """
    print("Got called back with %d and %d" % (a, b))
    return a + b

# Now we can assign the callback to a ctypes callback variable.
my_callback = FUNTYPE(my_c_callback)

# And now we can pass it to the C function.
lib.call_back(my_callback)

# We can also call it directly.
print("Direct result:", my_callback(5, 3))
</code>

