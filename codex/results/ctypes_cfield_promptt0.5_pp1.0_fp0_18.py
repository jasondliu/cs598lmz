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

class POINT_AND_RECT(ctypes.Structure):
    _fields_ = [("pt", POINT),
                ("rect", RECT)]

par = POINT_AND_RECT()
par.pt.x = 10
par.pt.y = 20
par.rect.left = 30
par.rect.top = 40
par.rect.right = 50
par.rect.bottom = 60
print("par.pt.x =", par.pt.x)
print("par.pt.y =", par.pt.y)
print("par.rect.left =", par.rect.left)
print("par.rect.
