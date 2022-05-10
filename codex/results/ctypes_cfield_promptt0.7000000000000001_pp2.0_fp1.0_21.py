import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_int),
        ("top", ctypes.c_int),
        ("right", ctypes.c_int),
        ("bottom", ctypes.c_int),
        ("top_left", POINT),
        ("bottom_right", POINT)]

# Test ctypes.CField
class FOO(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int),
        ("callback", ctypes.CFUNCTYPE(ctypes.c_int, RECT)),
    ]

# Test ctypes.CArray
class FOO2(ctypes.Structure):
    _fields_ = [
        ("p", ctypes.c_void_p),
        ("x", ctypes
