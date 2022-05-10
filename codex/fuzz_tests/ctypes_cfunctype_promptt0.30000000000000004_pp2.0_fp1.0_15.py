import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function with a callback
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# define the callback
@prototype
def py_callback(arg):
    print("py_callback", arg)
    return arg + 42

# register the callback
lib.set_callback(py_callback)

# call the callback
print(lib.call_callback(5))
