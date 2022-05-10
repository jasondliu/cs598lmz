import ctypes
# Test ctypes.CField
try:
    from ctypes import CField
except ImportError:
    import _ctypes_test
    CField = _ctypes_test.CField

class CFUnion(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char)]

class CFUnion1(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                (None, ctypes.c_int),
                ("b", ctypes.c_char)]

class CFUnion2(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                (None, ctypes.c_int),
                ("b", ctypes.c_char),
                (None, ctypes.c_int),
                ("c", ctypes.c_int)]

class CFUnion3(ctypes.Union):
    _fields_ = [("a", ctypes.c_longlong),
                (None, ctypes.c_longlong),
                ("b", c
