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

lib.pass_in_a_callback(callback)

# This is a function that returns a function pointer.
lib.return_a_callback.restype = CALLBACK

callback = lib.return_a_callback()
print(callback(42))

# This is a function that takes a function pointer as an argument
# and returns it.
lib.pass_in_a_callback_and_return_it.argtypes = [CALLBACK]
lib.pass_in_a_callback_and_return_it.restype = CALLBACK

callback = lib.pass_in_a_callback_and_return_it(callback)

