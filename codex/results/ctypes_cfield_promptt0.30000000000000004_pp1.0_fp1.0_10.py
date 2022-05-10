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
    _fields_ = [("length", ctypes.c_uint32),
                ("flags", ctypes.c_uint32),
                ("showCmd", ctypes.c_uint32),
                ("ptMinPosition", POINT),
                ("ptMaxPosition", POINT),
                ("rcNormalPosition", RECT)]

# Test ctypes.CArray
class RGBQUAD(ctypes.Structure):
    _fields_ = [("rgbBlue", ctypes.c_byte),
                ("rgbGreen", ctypes.c_byte),
                ("rgbRed
