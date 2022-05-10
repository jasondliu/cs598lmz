import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    def __init__(self, value):
        ctypes.c_int.__init__(self, value)

class Y(ctypes.c_int):
    def __init__(self):
        ctypes.c_int.__init__(self)

class Z(ctypes.c_int):
    def __init__(self):
        ctypes.c_int.__init__(self)

    def __repr__(self):
        return "int(%r)" % (int(self),)

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

    def __init__(self, value=None):
        if value:
            self.x, self.y, self.z = value
        else:
            self.x = self.y = self.z = 0

class Flags(ctypes.c_int):

