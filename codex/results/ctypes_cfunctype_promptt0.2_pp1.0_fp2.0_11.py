import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test calling a function with a function pointer argument
#

# A function taking a function pointer argument
functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# A function taking a function pointer argument
lib.my_callback.argtypes = [functype]
lib.my_callback.restype = ctypes.c_int

# A function taking a function pointer argument
def my_callback(arg):
    return arg

# Call the function
res = lib.my_callback(my_callback)
print(res)

#
# Test calling a function with a function pointer argument
#

# A function taking a function pointer argument
functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# A function taking a function pointer argument
lib.my_callback.argtypes = [functype]
lib.my_callback.rest
