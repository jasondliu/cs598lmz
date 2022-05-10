import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CALLBACK
def callback(arg):
    print("callback called with", arg)
    return arg + 1

lib.call_callback.argtypes = (CALLBACK, ctypes.c_int)
lib.call_callback.restype = ctypes.c_int

print(lib.call_callback(callback, 1))

# This is a function that takes a function pointer as an argument
# and returns it.
lib.return_callback.restype = CALLBACK

callback2 = lib.return_callback()
print(callback2(2))

# This is a function that takes a function pointer as an argument
# and returns it.
lib.return_callback2.restype = CALLBACK

callback3 = lib.return_callback2(
