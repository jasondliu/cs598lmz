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

    def __getattribute__(self, name):
        if name == 'x':
            return object.__getattribute__(self, '_x')
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'x':
            object.__setattr__(self, '_x', value)
        else:
            object.__setattr__(self, name, value)

class C3(object):
    def __init__(self):
        self.x = 0

    def __getattribute__(self, name):
        if name == 'x':
            return object.__getattribute__(self, '_x')
        return object.__getattribute__(self, name)

class C4(object):
    def __init__(self):
        self.x = 0

   
