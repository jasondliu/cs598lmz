import ctypes
# Test ctypes.CFUNCTYPE
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "POINT(%d, %d)" % (self.x, self.y)

