import ctypes
# Test ctypes.CFUNCTYPE
#
# The CFUNCTYPE is the same as CFUNCTYPE(None),
# except that it uses a default argument instead of a keyword argument.
#
# CPython issue #18667: ctypes.CFUNCTYPE(None, ...) is broken.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

f = lib.my_callback
f.argtypes = None, ctypes.c_int
f.restype = None

p = ctypes.CFUNCTYPE(None, ctypes.c_int)(f)
p(2)

lib.call_my_callback(p)

# test default arg
f = lib.my_callback
f.argtypes = None, ctypes.c_int
f.restype = None

p = ctypes.CFUNCTYPE(None)(f)
p(2)

lib.call_my_callback(p)

# test default arg and keyword arg
f = lib.my_callback
f.argtypes = None
