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

class RECT_FLOAT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_float),
                ("top", ctypes.c_float),
                ("right", ctypes.c_float),
                ("bottom", ctypes.c_float)]

class RECT_DOUBLE(ctypes.Structure):
    _fields_ = [("left", ctypes.c_double),
                ("top", ctypes.c_double),
                ("right", ctypes.c_double),
                ("bottom", ctypes.c_double)]

class RECT_INT(ctypes.Structure
