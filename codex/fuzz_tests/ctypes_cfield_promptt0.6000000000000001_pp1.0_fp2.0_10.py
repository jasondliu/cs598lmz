import ctypes
# Test ctypes.CField
class CTypesCField(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_short),
        ("y", ctypes.c_short),
    ]

class CTypesCFloatField(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]

class CTypesCDoubleField(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
    ]

# Test ctypes.c_char_p
class CTypesCCharP(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_char_p),
    ]

# Test ctypes.c_void_p
class CTypesCVoidP(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_void_p),
    ]

# Test ctypes.c_w
