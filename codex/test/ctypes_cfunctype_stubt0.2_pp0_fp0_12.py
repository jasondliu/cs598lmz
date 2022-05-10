import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class X(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class Y(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class Z(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class A(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class B(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

class C(object):
    def __init__(self, x):
        self.x = x
    def __call__(self):
        return self.x

