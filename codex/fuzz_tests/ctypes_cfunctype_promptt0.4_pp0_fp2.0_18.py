import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

#
# Test calling a function with a function pointer argument
#

# Prototype a function with a function pointer argument
# The function pointer must have the same argument and result types
# as the function it is passed to.
CALLBACKFUNC = CFUNCTYPE(c_int, c_int)

def callback(value):
    print("callback called with", value)
    return value + 42

# Register the callback with a foreign function
lib.set_callback(CALLBACKFUNC(callback))

# Call the foreign function
lib.call_callback(5)

#
# Test calling a function with a function pointer result
#

# Prototype a function with a function pointer result
GETCALLBACK = CFUNCTYPE(CALLBACKFUNC)

# Register the callback with a foreign function
lib.set_getcallback(GETCALLBACK(lambda: callback))

# Call the foreign function
lib.call_getcallback(5)

#
# Test calling
