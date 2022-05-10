import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class U(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __getattr__(self, name):
        if name == "x":
            return self.x
        raise AttributeError

class V(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __setattr__(self, name, value):
        if name == "x":
            self.x = value
        raise AttributeError

class W(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    def __getattr__(self, name):
        if name == "x":
            return self.x
        raise AttributeError
    def __setattr__(self, name, value):
        if name == "x":
            self.x = value
        raise AttributeError

class
