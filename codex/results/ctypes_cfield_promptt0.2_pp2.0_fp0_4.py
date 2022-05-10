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

class WINDOWPOS(ctypes.Structure):
    _fields_ = [("hwnd", ctypes.c_int),
                ("hwndInsertAfter", ctypes.c_int),
                ("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("cx", ctypes.c_int),
                ("cy", ctypes.c_int),
                ("flags", ctypes.c_int)]

class NMHDR(ctypes.Structure):
    _fields_ = [("hwndFrom", ctypes.c_int),
                ("idFrom", ctypes.c_
