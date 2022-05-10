import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

def main():
    s = S(1, 2)
    print "s.x =", s.x
    print "s.y =", s.y
    print "s.x + s.y =", s.x + s.y
    print "s.x * s.y =", s.x * s.y
    print "s.x / s.y =", s.x / s.y
    print "s.x % s.y =", s.x % s.y
    print "s.x << s.y =", s.x << s.y
    print "s.x >> s.y =", s.x >> s.y
    print "s.x & s.y =", s.x & s.y
    print "s.x | s.y =", s.x | s.y
    print "s.x ^ s.y =",
