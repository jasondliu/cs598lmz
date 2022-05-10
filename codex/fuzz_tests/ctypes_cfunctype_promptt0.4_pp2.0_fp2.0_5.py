import ctypes
# Test ctypes.CFUNCTYPE
def my_callback(a, b):
    return a + b

# This is the prototype of the callback function.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function that will call our callback.
def call_my_callback(cb, a, b):
    return cb(a, b)

# Create the callback.
cb = CALLBACK(my_callback)

# Call the callback.
print(call_my_callback(cb, 1, 2))

# Test ctypes.WINFUNCTYPE
def my_callback(a, b):
    return a + b

# This is the prototype of the callback function.
CALLBACK = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the function that will call our callback.
def call_my_callback(cb, a, b):
    return cb(a, b)

# Create
