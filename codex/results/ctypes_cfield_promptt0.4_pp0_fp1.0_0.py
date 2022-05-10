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
    _fields_ = [("pt", POINT * 10),
                ("rc", RECT * 10)]

# Test ctypes.CArray
class MY_ARRAY(ctypes.Structure):
    _fields_ = [("array", ctypes.c_int * 10)]

# Test ctypes.CArray and ctypes.CField
class MY_ARRAY_FIELD(ctypes.Structure):
    _
