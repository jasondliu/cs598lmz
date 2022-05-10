import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class T(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def f(a, b, c):
    return a + b + c

#
# test with builtin types
#

