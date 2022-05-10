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

class WINDOW(ctypes.Structure):
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int),
                ("visible", ctypes.c_bool),
                ("point", POINT),
                ("rect", RECT)]

w = WINDOW()
w.point = POINT(1,2)
w.rect = RECT(1,2,3,4)
print(w)
print(w.point)
print(w.rect)


