import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    def __repr__(self):
        return "S(%s, %s)" % (self.x, self.y)

class Color(S):
    pass

class Point(S):
    pass

class Rect(ctypes.Structure):
    _fields_ = [("origin", Point), ("size", Point)]

class Window(ctypes.Structure):
    _fields_ = [("origin", Point), ("size", Point), ("color", Color)]

