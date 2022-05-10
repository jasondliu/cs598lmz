import ctypes
# Test ctypes.CFUNCTYPE to create a callback function

# Create a callback function
# Callback function must accept a single argument
# (and return a single value)
# Note that Python does not have a type for C pointers (void*)
# So we pass a Python integer (int) as the callback argument
# and cast to a C pointer in the callback function
# (This will not work if the callback is called from C code)
# We also need to cast the Python integer to a C integer (c_int)
# to match the prototype of the callback function
CBFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print("Callback function called with x =", x)
    return x * x

# Create the callback function
cb = CBFUNC(callback)

# Call the callback function
print('Result of calling cb:', cb(2))

# This is equivalent to the following code:
#CBFUNC(callback)(2)

# The following code would not work:
#CBFUNC(callback)()
#callback()
