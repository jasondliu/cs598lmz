import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("A", ctypes.c_char * 8),
                ("B", ctypes.c_char * 8),
                ("C", ctypes.c_char * 5),
                ("D", ctypes.c_ubyte)]
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_short),
                ("y", ctypes.c_short)]
class _RECT(ctypes.Structure):
    _fields_ = [("line", POINT),
                ("text", POINT)]
class RECT(ctypes.Structure):
    _fields_ = [("center", POINT),
                ("extent", POINT),
                ("line", ctypes.CField(_RECT)),
                ("text", ctypes.CField(_RECT))]

# Test ctypes.array
class array(ctypes.Structure):
    _fields_ = [("A", ctypes.c_char * 8),
                ("B", ctypes.c_char * 8 * 4),
