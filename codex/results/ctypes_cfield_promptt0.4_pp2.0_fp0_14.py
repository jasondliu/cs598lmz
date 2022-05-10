import ctypes
# Test ctypes.CField

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

class POINT_PTR(ctypes.POINTER(POINT)):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT_PTR(ctypes.POINTER(RECT)):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

class POINT_PTR_PTR(ctypes.POINTER(POINT_PTR)):
    _fields_ =
