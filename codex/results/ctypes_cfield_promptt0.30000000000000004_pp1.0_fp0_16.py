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

# Test ctypes.CArray
class MyArray(ctypes.Array):
    _length_ = 10
    _type_ = ctypes.c_int

# Test ctypes.CString
class MyString(ctypes.c_char_p):
   
