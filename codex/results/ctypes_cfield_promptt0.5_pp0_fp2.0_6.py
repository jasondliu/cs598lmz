import ctypes
# Test ctypes.CField instance

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

    def __repr__(self):
        return "POINT(%d, %d)" % (self.x, self.y)

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

    def __repr__(self):
        return "RECT(%d, %d, %d, %d)" % (self.left, self.top, self.right, self.bottom)

class POINT2(ctypes.Structure):
    _fields_ = [("pt", POINT),
                ("padding", ctypes.c_long)]

    def __repr__(self):
        return "POINT2(%d, %d, %d)"
