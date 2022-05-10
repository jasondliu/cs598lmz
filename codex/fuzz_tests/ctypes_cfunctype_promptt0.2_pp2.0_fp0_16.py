import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

CALLBACK = CALLBACKFUNC(callback)

lib.pass_in_a_callback(CALLBACK)

# This is a function that returns a function pointer.

lib.return_a_callback.restype = CALLBACKFUNC

CALLBACK = lib.return_a_callback()

print("CALLBACK", CALLBACK)
print("CALLBACK(12)", CALLBACK(12))

# This is a function that takes a function pointer as argument
# and calls it.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_
