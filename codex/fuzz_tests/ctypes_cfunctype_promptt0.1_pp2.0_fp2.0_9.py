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

result = func(42)
if result != 42:
    raise Exception("%d != 42" % result)

#
# Now test a function with a structure result
#

# struct foo func(int)
class foo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

prototype = ctypes.CFUNCTYPE(foo, ctypes.c_int)

func = prototype((b"func_foo_int", lib))

result = func(42)
if result.a != 42 or result.b != 42:
    raise Exception("%d != 42" % result
