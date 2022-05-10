import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a ctypes.Structure subclass
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# This is a ctypes.Structure subclass
class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

# This is a ctypes.Structure subclass
class PAINTSTRUCT(ctypes.Structure):
    _fields_ = [("hdc", ctypes.c_int),
                ("fErase", ctypes.c_int),
                ("rcPaint", RECT),
                ("fRestore", ctypes.c_int),
                ("fIncUpdate", ctypes.c_int),
                ("rgbReserved", ctypes.c_char * 32)]

# This is a c
