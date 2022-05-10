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

rect = Rect(Point(1.0, 1.0), Point(2.0, 2.0))
rect.origin = Point(10.0, 10.0)
print(rect)

window = Window(Point(1.0, 1.0), Point(2.0, 2.0), Color(1.0, 1.0))
print(window)
