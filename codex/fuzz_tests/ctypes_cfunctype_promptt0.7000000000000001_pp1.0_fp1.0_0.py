import ctypes
# Test ctypes.CFUNCTYPE
#
# A ctypes callback is a Python object that is called when a
# C function pointer is invoked.  This is useful for implementing
# C callbacks, for example for an asynchronous notification, or
# a C library function taking a function pointer argument.
#
# This test demonstrates that ctypes callback functions work.
#
import _ctypes_test
lib = _ctypes_test.dll

# A CFUNCTYPE factory function creates callbacks with the specified
# argument and return types.
CallbackType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The first argument is the return type of the callback.
# The rest of the arguments are the argument types.

# This creates a callback-function.
# Passing a Python callable object to the factory function
# creates a callable ctypes object, which when called,
# calls the Python callable.
def py_add(a, b):
    return a+b

# Create a ctypes callback object from the Python function.
add2 = CallbackType
