import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# First test a simple function
#

# This is the prototype of the function we are going to call
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function we are going to call
func = prototype(("_testfunc_callback", lib))

# This is the function we are going to pass to the function we are
# going to call
def func_callback(value):
    print("func_callback", value)
    return value + 1

# Now call the function
result = func(func_callback)
print(result)

#
# Now test a function that takes a pointer argument
#
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))
func = prototype(("_testfunc_callback_ptr", lib))

def func_callback_ptr(pointer):
    print("func_callback
