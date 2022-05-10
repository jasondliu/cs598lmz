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

class WINDOWPLACEMENT(ctypes.Structure):
    _fields_ = [("length", ctypes.c_uint),
                ("flags", ctypes.c_uint),
                ("showCmd", ctypes.c_uint),
                ("ptMinPosition", POINT),
                ("ptMaxPosition", POINT),
                ("rcNormalPosition", RECT)]

class WINDOWINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("rcWindow", RECT),
                ("rcClient", RECT),
                ("dwStyle", ctypes.c_uint
