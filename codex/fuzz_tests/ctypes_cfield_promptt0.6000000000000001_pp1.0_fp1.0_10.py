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

class POINT_ARRAY(ctypes.Structure):
    _fields_ = [("points", POINT*10),
                ("count", ctypes.c_int)]

class RECT_ARRAY(ctypes.Structure):
    _fields_ = [("rects", RECT*10),
                ("count", ctypes.c_int)]

class RECT_ARRAY_ARRAY(ctypes.Structure):
    _fields_ = [("rects", RECT_ARRAY*10),
                ("count", ctypes.c_int)]

class POINT_RECT(ctypes.Structure):
   
