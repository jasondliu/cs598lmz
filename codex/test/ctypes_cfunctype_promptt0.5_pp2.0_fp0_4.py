import ctypes
# Test ctypes.CFUNCTYPE()

# This is the prototype of the function we'll call.
PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we'll call.
def python_callback(x):
    print("Called back with", x)
    return x

# Build a wrapper function around the Python function.
# This function has the same prototype as the function
# we are going to call.
c_callback = PROTOTYPE(python_callback)

# Call the C function.
print("Calling C function")
