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

class PAINTSTRUCT(ctypes.Structure):
    _fields_ = [("hdc", ctypes.c_int),
                ("fErase", ctypes.c_int),
                ("rcPaint", RECT),
                ("fRestore", ctypes.c_int),
                ("fIncUpdate", ctypes.c_int),
                ("rgbReserved", ctypes.c_char * 32)]

ps = PAINTSTRUCT()

# Test ctypes.CArray
class A(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int * 2)]

# Test c
