import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class C2(object):
    def __init__(self, x):
        self.x = x
        self.y = x

class C3(object):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x

class C4(object):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x
        self.t = x

class C5(object):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x
        self.t = x
        self.u = x

class C6(object):
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x
        self.t = x
        self.u = x
       
