import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert fun() == 1

class A(object):
    def __init__(self):
        self.x = 1
    def f(self):
        return self.x

a = A()
assert a.f() == 1

class B(object):
    def __init__(self):
        self.x = 1
    def f(self):
        return self.x

b = B()
assert b.f() == 1

class C(object):
    def __init__(self):
        self.x = 1

    @classmethod
    def f(cls):
        return cls.x

c = C()
