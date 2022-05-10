import ctypes
# Test ctypes.CField

libc = ctypes.CDLL(ctypes.util.find_library("c"))

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

# An 'out' parameter
libc.PtInRect.argtypes = (ctypes.POINTER(RECT), POINT)
libc.PtInRect.restype = ctypes.c_int

# An 'in' parameter
libc.RectInRect.argtypes = (RECT, RECT)
libc.RectInRect.restype = ctypes.c_int

r = RECT(0, 0, 10, 10)
p = POINT(5, 5)

print(libc.PtInRect
