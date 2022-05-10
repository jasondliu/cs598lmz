import ctypes
# Test ctypes.CFUNCTYPE() as a result of a call

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)
prototypes = (
    (ctypes.c_int, []),
    (ctypes.c_float, []),
    (ctypes.c_void_p, []),
    (ctypes.POINTER(ctypes.c_float), []),
    (ctypes.POINTER(ctypes.POINTER(ctypes.c_float)), []),
    (ctypes.CFUNCTYPE(ctypes.c_int), []),
    (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float), []),
    (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float), [1.5]),
    (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_float, ctypes.c_double), []),
    (ctypes.CFUNCTYPE(ctypes.c_int, ctypes
