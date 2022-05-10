import types
# Test types.FunctionType

# Test FunctionType's __new__
class A(object):
    def __new__(cls, *args, **kwargs):
        return super(A, cls).__new__(cls)

def f():
    pass

def g(self):
    pass

def h(self, a=1, b=2):
    pass

def i(self, a, b, c=3):
    pass

def j(self, a, b, c, d=4):
    pass

def k(self, a, b, c, d, e=5):
    pass

def l(self, a, b, c, d, e, f=6):
    pass

def m(self, a, b, c, d, e, f, *args):
    pass

def n(self, a, b, c, d, e, f, *args, **kwargs):
    pass

def o(self, a, b, c, d, e, f, *args, **kwargs):
    pass


