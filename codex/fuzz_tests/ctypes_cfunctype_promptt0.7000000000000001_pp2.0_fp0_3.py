import ctypes
# Test ctypes.CFUNCTYPE.

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# XXX: _ctypes_test.__file__ is an empty string under Jython, so we need
# to use the actual DLL name
if not lib._name:
    lib._name = "ctypes_test.pyd"

def must_raise(exc, func, *args):
    try:
        func(*args)
    except exc as e:
        pass
    else:
        print(func.__name__, "didn't raise", exc)

# test function with explicit argtypes
prototype = CFUNCTYPE(c_int, c_int)

paramflags = ((1, "value"),)

#
# Test calling the function prototype
#
res = prototype(42, 43)
if res != 42:
    raise RuntimeError("prototype call returned %s" % (res,))

res = prototype((42,), (43,))
if res != 42:
    raise RuntimeError("prototype call returned %s" % (res,))

