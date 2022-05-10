import ctypes
# Test ctypes.CField
class _FIELD(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class _FIELD2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class _FIELD3(ctypes.Union):
    _fields_ = [("alias_field", ctypes.c_int),
                ("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class _FIELD4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

_FIELD4
