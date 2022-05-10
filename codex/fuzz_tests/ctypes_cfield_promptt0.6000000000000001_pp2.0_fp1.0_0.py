import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = POINT(5,6)
print(pt.x, pt.y)

class POINT2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("pt", POINT)]

pt2 = POINT2(1,2,pt)
print(pt2.x, pt2.y, pt2.pt.x, pt2.pt.y)

# Test ctypes.CField
class POINT3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("pt", POINT),
                ("pt2", POINT2)]

pt3 = POINT3(1,2,pt,pt2)
print(pt3.x, pt3.y, pt3.
