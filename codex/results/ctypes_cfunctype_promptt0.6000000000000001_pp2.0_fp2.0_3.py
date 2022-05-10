import ctypes
# Test ctypes.CFUNCTYPE
def callback(x):
    print x
    return x + 1

# The CFUNCTYPE() function automatically determines
# how to convert the Python types to C data types.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Convert the Python callback function into C pointer.
c_callback = CMPFUNC(callback)

# This is the prototype of the C function
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Convert the Python callback function into C pointer.
c_callback = CMPFUNC(callback)

# Call the C function from Python
print c_callback(2)

# Convert the Python callback function into C pointer.
c_callback = CMPFUNC(callback)

# Call the C function from Python
print c_callback(3)

# Convert the Python callback function into C pointer.
c_callback = CMPFUNC(callback)

# Call the C function from Python
print c_callback
