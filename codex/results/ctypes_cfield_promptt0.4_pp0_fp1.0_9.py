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

class POINT_RECT(ctypes.Structure):
    _fields_ = [("pt", POINT),
                ("rc", RECT)]

class POINT_RECT_ARRAY(ctypes.Structure):
    _fields_ = [("pt", POINT * 2),
                ("rc", RECT * 2)]

class POINT_RECT_PTR(ctypes.Structure):
    _fields_ = [("pt", POINT * 2),
                ("rc", RECT * 2)]

class POINT_RECT_PTR_PTR(ctypes.Structure):
    _fields_ = [("pt", PO
