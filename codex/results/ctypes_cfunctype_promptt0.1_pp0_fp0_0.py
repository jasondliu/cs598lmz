import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# First test a function with a simple result type
#

# int func(int)
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

func = prototype((b"func_int_int", lib))

# call the function
result = func(42)
if result != 42:
    raise Exception("function call failed")

#
# Now test a function with a more complicated result type
#

# struct foo func(int)
class foo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_double)]

prototype = ctypes.CFUNCTYPE(foo, ctypes.c_int)

func = prototype((b"func_foo_int", lib))

# call the function
result = func(42)
if result.a != 42:
    raise Exception("function call failed")

