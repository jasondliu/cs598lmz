import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX: This test is not complete, it only tests the basic
# functionality.

# a function
def func(x):
    return x * 2

# a function pointer type
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call the function pointer
lib.call_function(CFuncPtr(func), 5)

# call the function pointer through a function
lib.call_funcptr(CFuncPtr(func))

# call the function pointer through a pointer
lib.call_funcptr_indirect(CFuncPtr(func))

# call the function pointer through a pointer, passing a pointer
lib.call_funcptr_indirect_arg(CFuncPtr(func))

# call the function pointer through a pointer, passing a pointer
# to a pointer
lib.call_funcptr_indirect_arg_indirect(CFuncPtr(func))

# call the function pointer through a
