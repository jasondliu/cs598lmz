import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# Test calling a function with a prototype
#

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The prototype is used to convert the arguments
i = prototype(("add", lib), ((1, 2),))
if i != 3:
    raise RuntimeError("%d != 3" % i)

#
# Test calling a function without a prototype
#
i = lib.add(1, 2)
if i != 3:
    raise RuntimeError("%d != 3" % i)

#
# Test calling a function with a prototype and keyword arguments
#
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
i = prototype(("add", lib), (2,), dict(b=3))
if i != 5:
    raise RuntimeError("%d != 5" % i)

#
#
