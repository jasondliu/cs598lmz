import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

class D(object):
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x

def set_x(self, x):
    self.x = x

C.set_x = set_x
D.set_x = set_x

def get_x(self):
    return self.x

C.get_x = get_x
D.get_x = get_x

def get_x_string(self):
    return self.x

C.get_x_string = get_x_string
D.get_x_string = get_x_string

def set_x_string(self, x):
    self.x = x

C.set_x_string = set_x_string
D.set_x_string = set_x_string

class E(
