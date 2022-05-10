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
class POINT_RECT(ctypes.Union):
    _fields_ = [("point", POINT),
                ("rect", RECT)]
pr = POINT_RECT()
pr.point.x = 1
pr.point.y = 2
print pr.point.x, pr.point.y
pr.rect.left = 3
pr.rect.right = 4
print pr.rect.left, pr.rect.right
