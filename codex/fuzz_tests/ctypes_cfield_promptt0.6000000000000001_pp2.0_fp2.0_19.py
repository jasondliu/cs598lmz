import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int),
                ("w", ctypes.c_int)]
    _anonymous_ = ("z", "w")

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]
    _anonymous_ = ("left", "top")

class POINT_PTR(ctypes.POINTER(POINT)):
    _type_ = "i"
    _subtype_ = POINT

class RECT_PTR(ctypes.POINTER(RECT)):
    _type_ = "i"
    _subtype_ = RECT

class Test(ctypes.Structure):
    _fields_ = [("point", POINT_PTR),

