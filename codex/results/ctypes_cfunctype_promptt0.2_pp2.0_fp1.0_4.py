import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Define a callback function
@prototype
def callback(i):
    print("callback", i)
    return i + 1

# Call the function with the callback
lib.set_callback(callback)

# Call the callback directly
print(callback(1))

# Call the callback via the function
print(lib.call_callback(1))

# Call the callback via the function pointer
print(lib.call_callback_ptr(callback, 1))

# Call the callback via the function pointer, using the prototype
print(prototype(lib.call_callback_ptr)(1))

# Call the callback via the function pointer, using the prototype
# and a foreign function
print(prototype(lib.call_callback_ptr)(1))

# Call the callback via the function pointer, using the prototype
# and a foreign function

