import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

class A(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class B(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class C(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

def test_simple():
    assert f(1) == 1
    assert f(1) == 1
   
