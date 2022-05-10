import ctypes
# Test ctypes.CField.from_param

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

    def __repr__(self):
        return "(%d, %d, %d, %d)" % (self.left, self.top, self.right, self.bottom)

class POINTARRAY(ctypes.Structure):
    _fields_ = [("nPoints", ctypes.c_long),
                ("points", ctypes.POINTER(POINT))]

    def __repr__(self):
        return "(%d, %s)" % (self.n
