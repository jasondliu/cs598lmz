import ctypes
ctypes.cast(1, ctypes.py_object)

# Test generation of pythonic code (functions, classes, metaclasses)

class A(object):
    def f(self):
        pass

def f():
    pass

def f(*args):
    pass

def f(**kwargs):
    pass

def f(*args, **kwargs):
    pass

def f(x, *args, **kwargs):
    pass

class Empty:
    pass

# Old-style class
class Empty:
    "empty"
    pass

class Single:
    "one method"
    def f(self, x):
        pass

class B(object):
    "one method"
    def f(self, x):
        pass

class C(object):
    def f(self, x):
        pass
    def g(self, x):
        pass

class D(object):
    def __init__(self, x):
        pass
    def f(self, x):
        pass

class E(object):
    def
