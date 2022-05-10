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

class POINT_RECT(ctypes.Union):
    _fields_ = [("pt", POINT),
                ("rc", RECT)]

class POINT_RECT_2(ctypes.Union):
    _fields_ = [("pt", POINT),
                ("rc", RECT),
                ("ptrc", POINT_RECT)]

class POINT_RECT_3(ctypes.Union):
    _fields_ = [("pt", POINT),
                ("rc", RECT),
                ("ptrc", POINT_RECT),
                ("ptrc2", POINT_RECT_2)]

class POINT_RECT_4
