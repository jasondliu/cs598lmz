import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the dll.

def callback(number):
    print("callback called with", number)
    return number + 1

# This is the function in the dll:

lib.set_callback.argtypes = ctypes.c_int, CALLBACKFUNC
lib.set_callback.restype = None

# Now call the dll function.  The integer it returns is the
# result of calling the callback function.

print(lib.set_callback(42, CALLBACKFUNC(callback)))

# Now call the dll function again, but pass None as the callback.
# This should raise a TypeError.

try:
    print(lib
