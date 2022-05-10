import ctypes
# Test ctypes.CFUNCTYPE with a None return type (this should be void).

import _ctypes_test
lib = ctypes.CDLL(_ctypes_test.__file__)

# None is the same as void:
f = ctypes.CFUNCTYPE(None)(("bar", lib), ())
f()

f = ctypes.CFUNCTYPE(ctypes.c_int)(("bar", lib), ())
if f() != 0:
    raise RuntimeError("CFUNCTYPE with None return type failed")

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("bar", lib), ())
if f(1) != 1:
    raise RuntimeError("CFUNCTYPE with None return type failed")

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(("bar", lib),
                                                              ())
if f(1, 2) != 3:
    raise RuntimeError("CFUNCTYPE with None return type failed")

f
