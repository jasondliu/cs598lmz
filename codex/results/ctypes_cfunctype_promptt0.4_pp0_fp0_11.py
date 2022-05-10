import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# XXX This test is incomplete

def test(restype, argtypes, *args):
    func = ctypes.CFUNCTYPE(restype, *argtypes)(("testfunc", lib), ())
    result = func(*args)
    print(result)
    print(func.restype, func.argtypes)
    print(func.errcheck)

test(ctypes.c_int, [ctypes.c_int, ctypes.c_int], 3, ctypes.c_int(4))
test(ctypes.c_int, [ctypes.c_int, ctypes.c_int], 3, 4)
test(ctypes.c_int, [ctypes.c_int, ctypes.c_int], 3, 4)
test(ctypes.c_int, [ctypes.c_int, ctypes.c_int], 3, 4)
test(ctypes.c_int, [ctypes.c_int,
