import ctypes
# Test ctypes.CFUNCTYPE().

import _ctypes_test

restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

expect = 0

for args, result in (((16,), 0),
                     ((1,), 1),
                     ((0,), None)):
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = restype(("_testfunc_return_type", dll), args)
    result = func(*args)
    if result != expect:
        raise ctypes.Argumen
