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

def PtInRect(rect, pt):
    return (rect.left <= pt.x <= rect.right and
            rect.top <= pt.y <= rect.bottom)

rect = RECT(0, 0, 500, 500)
pt = POINT(100, 100)
print(PtInRect(rect, pt))

pt = POINT(1000, 1000)
print(PtInRect(rect, pt))

# Test alignment
import ctypes
class T(ctypes.Structure):
    _pack_ = 1
    _fields_ = [("b1", ctypes.c_ubyte),
                ("b
