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

for typ in ["c", "i", "l", "f", "d", "P"]:
    for argtypes in [[], [ctypes.c_int], [ctypes.c_int]*2,
                     [ctypes.c_int]*3, [ctypes.c_int]*4, [ctypes.c_int]*5,
                     [ctypes.c_int]*6, [ctypes.c_int]*7, [ctypes
