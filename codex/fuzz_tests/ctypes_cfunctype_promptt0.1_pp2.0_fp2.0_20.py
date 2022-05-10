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

lib.pass_in_callback(callback)

# This is a function that returns a function pointer
# The returned function pointer takes an integer argument and returns
# the argument incremented by 1.
lib.return_callback.restype = CALLBACK

f = lib.return_callback()
print(f(42))

# This is a function that takes a function pointer as an argument
# and returns it.
lib.pass_callback_return_callback.argtypes = (CALLBACK,)
lib.pass_callback_return_callback.restype = CALLBACK

f = lib.pass_callback_return_callback(callback)
print(f(
