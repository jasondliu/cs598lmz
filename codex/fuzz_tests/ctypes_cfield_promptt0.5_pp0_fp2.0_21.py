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
    _fields_ = [("length", ctypes.c_int),
                ("flags", ctypes.c_int),
                ("showCmd", ctypes.c_int),
                ("ptMinPosition", POINT),
                ("ptMaxPosition", POINT),
                ("rcNormalPosition", RECT)]

wp = WINDOWPLACEMENT()
wp.length = ctypes.sizeof(WINDOWPLACEMENT)
wp.flags = 0
wp.showCmd = 1
wp.ptMinPosition.x = 5
wp.ptMinPosition.y = 6
wp
