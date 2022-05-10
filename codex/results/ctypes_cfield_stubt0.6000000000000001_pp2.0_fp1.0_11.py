import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1

ctypes.CField = type(S.x)

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
    def __del__(self):
        pass

ctypes.CField = type(S.x)

class V(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
    def __del__(self):
        pass
    def meth(self):
        pass

ctypes.CField = type(S.x)

class W(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self):
        self.x = 1
    def
