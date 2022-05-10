import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 0

class C2(object):
    def __init__(self):
        self.x = 0
        self.y = 0

class C3(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class C4(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0

class C5(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.u = 0

class C6(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.u = 0
        self.v = 0

class C7(object
