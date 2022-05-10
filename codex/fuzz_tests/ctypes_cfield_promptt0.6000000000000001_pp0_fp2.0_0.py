import ctypes
# Test ctypes.CField
import ctypes.util
ctypes.util.find_library('c')

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

class POINT_P(ctypes.POINTER(POINT)):
    pass

class RECT_P(ctypes.POINTER(RECT)):
    pass

# Test ctypes.POINTER(ctypes.Array(...)), ...

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_double)]

class Y(ctypes.Structure):
    _fields_ = [("x", X * 5),
                ("y", ctypes.
