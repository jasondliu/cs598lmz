import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class A(object):
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class B(A):
    pass

class C(A):
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class D(A):
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class E(A):
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return hash(self.x)

class F(A):
    def __eq__(self, other):
        return self.x == other.x
    def __hash__(self):
        return
