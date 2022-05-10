import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@prototype
def callback(i):
    print("callback", i)
    return i + 1

lib.call_with_callback(callback, 3)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE(None, ctypes.c_int)

@prototype
def callback(i):
    print("callback", i)

lib.call_with_callback(callback, 3)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE(None)

@prototype
def callback():
    print("callback")

lib.call_with_callback(callback)

# call a function with a CFUNCTYPE argument

prototype = ctypes.CFUNCTYPE
