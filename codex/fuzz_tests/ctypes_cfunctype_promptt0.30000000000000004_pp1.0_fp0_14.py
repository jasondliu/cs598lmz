import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# Call a function with a float argument, and return a float
f = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)(("testf", lib), ((1,),))
res = f(1.0)
if res != 2.0:
    raise RuntimeError("float return value is %f" % res)

# Call a function with a double argument, and return a double
d = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(("test", lib), ((1,),))
res = d(1.0)
if res != 2.0:
    raise RuntimeError("double return value is %f" % res)

# Call a function with a long double argument, and return a long double
ld = ctypes.CFUNCTYPE(ctypes.c_longdouble, ctypes.c_longdouble)(("testl", lib), ((1,),))
res =
