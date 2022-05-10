import types
# Test types.FunctionType, types.LambdaType, and types.BuiltinFunctionType

class A:
    def f(self): pass
    def g(self, a): pass
    def h(self, a, b): pass

class B:
    def __init__(self):
        self.ff = self.f
        self.gg = self.g
        self.hh = self.h

    def f(self): pass
    def g(self, a): pass
    def h(self, a, b): pass

class C:
    def __init__(self,x):
        self.x = x
        self.ff = self.f
        self.gg = self.g
        self.hh = self.h

    def f(self): pass
    def g(self, a): pass
    def h(self, a, b): pass

def f(): pass
def g(a): pass
def h(a, b): pass

def test():
    a = A()
    b = B()
    c = C(5)

    assert type(a.
