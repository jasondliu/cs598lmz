import ctypes
# Test ctypes.CFUNCTYPE
# Also tests ctypes.Structure and ctypes.Union

import _ctypes_test
dll = ctypes.CDLL(_ctypes_test.__file__)


class X(ctypes.Structure):
    _fields_ = [("c1", ctypes.c_char),
                ("c2", ctypes.c_char)]


class Y(ctypes.Structure):
    _fields_ = [("i", ctypes.c_int),
                ("p", ctypes.c_void_p)]


