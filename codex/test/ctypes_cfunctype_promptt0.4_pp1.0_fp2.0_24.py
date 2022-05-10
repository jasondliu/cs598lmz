import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

try:
    c_int_p = ctypes.POINTER(ctypes.c_int)
except TypeError:
    # XXX: This is a workaround for a bug in ctypes.
    c_int_p = ctypes.POINTER(ctypes.c_long)

def test(typ, restype, argtypes):
    func = ctypes.CFUNCTYPE(restype, *argtypes)(_ctypes_test.get_func(typ))
    func.restype = restype
    func.argtypes = argtypes
    return func

