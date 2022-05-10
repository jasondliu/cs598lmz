import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# first define a function that takes a function pointer as argument

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

# now call the function with the callback as argument

lib.call_function(CALLBACKFUNC(callback), 1)

# call a function with a function pointer result

# first define a function that returns a function pointer

lib.get_function.restype = CALLBACKFUNC

# now call the function and call the result

result = lib.get_function()
print("result is", result)
print("result(1) is", result(1))

# call a function with a function pointer result, and pass it
# as argument to another function

lib.call_function(lib.get_function(), 1)

