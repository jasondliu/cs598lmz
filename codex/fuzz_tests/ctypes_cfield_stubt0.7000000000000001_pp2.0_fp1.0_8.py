import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]
    def __init__(self):
        ctypes.Structure.__init__(self)
        self.x = 42

print S2()
