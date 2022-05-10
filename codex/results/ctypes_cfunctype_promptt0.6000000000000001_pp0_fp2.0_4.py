import ctypes
# Test ctypes.CFUNCTYPE
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "POINT(%d, %d)" % (self.x, self.y)

PointAdd = ctypes.CFUNCTYPE(POINT, POINT, POINT)(lambda p1, p2: POINT(p1.x + p2.x, p1.y + p2.y))
print(PointAdd(POINT(1, 2), POINT(3, 4)))

# Test ctypes.WINFUNCTYPE
stdcall_PointAdd = ctypes.WINFUNCTYPE(POINT, POINT, POINT)(PointAdd)
print(stdcall_PointAdd(POINT(1, 2), POINT(3, 4)))

# Test ctypes.PYFUNCTYPE
cdecl_PointAdd = c
