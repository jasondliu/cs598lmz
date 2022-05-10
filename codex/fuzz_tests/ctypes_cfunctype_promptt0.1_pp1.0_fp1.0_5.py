import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the dll.

def callback(i):
    print("callback", i)
    return i + 1

# Call the dll function.  The integer it returns is the result of
# calling the callback function.

res = lib.set_callback(CALLBACKFUNC(callback))
print("result", res)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# a pointer to a character.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)

# This is the function that we pass to
