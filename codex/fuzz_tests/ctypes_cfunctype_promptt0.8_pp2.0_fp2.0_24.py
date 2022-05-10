import ctypes
# Test ctypes.CFUNCTYPE.
#
# ctypes does not support arrays passed by value. The data must be passed
# as a pointer to a fixed size buffer.
#

import ctypes, _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

f = ctypes.CFUNCTYPE(None, ctypes.c_double * 3)(("f", lib))

d = (ctypes.c_double * 3) (1.0, 2.0, 3.0)

f(d)

if d[0] != 2.0 or d[1] != 4.0 or d[2] != 6.0:
    raise RuntimeError, d

f = ctypes.CFUNCTYPE(None, ctypes.c_float * 3)(("f", lib))

d = (ctypes.c_float * 3) (1.0, 2.0, 3.0)

f(d)

if d[0] != 2.0 or d[1] != 4.0 or d[2] != 6.0:

