import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(object):
    def __init__(self):
        self.x = 1

class D(object):
    def __init__(self):
        self.x = 1
    def __getattr__(self, name):
        return 2

class E(object):
    def __init__(self):
        self.x = 1
    def __getattribute__(self, name):
        return 2

class F(object):
    def __init__(self):
        self.x = 1
    def __getattr__(self, name):
        return 2
    def __getattribute__(self, name):
        return 3

class G(object):
    def __init__(self):
        self.x = 1
    def __getattribute__(self, name):
        return 2
    def __getattr__(self, name):
        return 3

class H(object):
    def __init__(self):
        self.x = 1
    def __getattribute__(self, name):
        return
