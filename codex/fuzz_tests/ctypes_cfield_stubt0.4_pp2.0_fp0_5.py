import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        print('getting', name)
        return super().__getattribute__(name)

class E(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        print('getting', name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return 42

class F(object):
    def __init__(self, x):
        self.x = x
    def __getattribute__(self, name):
        print('getting', name)
        try:
            return super().__getattribute__(name)
        except AttributeError:
            return 42
    def __setattr__(self, name, value):
        print('setting', name, 'to', value)
       
