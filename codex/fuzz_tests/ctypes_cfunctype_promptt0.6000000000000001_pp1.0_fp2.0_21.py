import ctypes
# Test ctypes.CFUNCTYPE(None) and ctypes.CFUNCTYPE(ctypes.c_int)
# without a prototype.

import _ctypes_test

dll = ctypes.CDLL(_ctypes_test.__file__)

func = ctypes.CFUNCTYPE(None)(("testfunc_noprototype", dll))
func()

func = ctypes.CFUNCTYPE(ctypes.c_int)(("testfunc_noprototype", dll))
assert func() == 42

try:
    func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
        ("testfunc_noprototype", dll))
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")
