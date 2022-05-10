import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have a simple signature: int()
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int)

# This is the function to call.
def callback():
    print("callback() called")
    return 42

# Call the function in lib, which takes a function pointer as argument.
lib.set_callback(CALLBACK(callback))

# Call the function in lib, which calls the function pointer.
result = lib.call_callback()
print("callback() returned", result)

# The following is a more complex example.  A function pointer is
# passed as argument to another function.  The called function calls
# the passed function pointer.

# This is the function to call.
def callback(n):
    print("callback() called with", n)
    return -n

# This is the function that takes a function pointer and an integer
# as arguments, and
