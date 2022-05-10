import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# this is a function that takes a function pointer as argument
# and calls it
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

@CALLBACKFUNC
def callback(arg):
    print("callback called with", arg)
    return arg + 3

lib.pass_func(callback)

# call a function with a function pointer result
# this is a function that returns a function pointer
# and calls it

lib.return_func.restype = CALLBACKFUNC

f = lib.return_func()
print("returned function pointer", f)
print("calling it now")
print(f(42))

# call a function with a function pointer result
# this is a function that returns a function pointer
# and calls it

lib.return_func2.restype = CALLBACKFUNC

f = lib.return_func2
