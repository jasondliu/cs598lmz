import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that is called by the function pointer.
def callback(i):
    print("callback", i)
    return i + 1

# This is the function that takes a function pointer as argument.
lib.pass_in_callback.argtypes = (CALLBACK,)
lib.pass_in_callback.restype = ctypes.c_int

# Call the function with the function pointer as argument.
result = lib.pass_in_callback(CALLBACK(callback))
print(result)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is
