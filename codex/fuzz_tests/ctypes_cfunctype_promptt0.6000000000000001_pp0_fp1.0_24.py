import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def func(a, b):
    print(a, b)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

callback = CALLBACK(func)

_ctypes_test.set_callback(callback)
_ctypes_test.call_callback(10, 20)

callback = CALLBACK(lambda a, b: print(a, b))
_ctypes_test.set_callback(callback)
_ctypes_test.call_callback(30, 40)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#   restype: The result type.
#   argtypes: A list of argument types.
#   use_errno: If True, the function will check for errors after the call.
#   use_last_error: If True, the function will check for Windows errors after the call.

# ctypes.CFUNCTYPE(None, c
