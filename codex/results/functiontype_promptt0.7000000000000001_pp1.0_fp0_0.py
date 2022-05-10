import types
# Test types.FunctionType
if types.FunctionType is not type(lambda: None):
    raise ImportError("types.FunctionType is not type(lambda: None)")

class A(object):
    def __init__(self, x):
        self.x = x

# Test @property
class B(object):
    @property
    def x(self):
        return 42
    @x.setter
    def x(self, value):
        pass
    @x.deleter
    def x(self):
        pass

# Test @staticmethod
class C(object):
    @staticmethod
    def f(x):
        return x

# Test @classmethod
class D(object):
    @classmethod
    def f(cls, x):
        return x

# Test @super
class E(object):
    def g(self, x):
        return x

class F(E):
    def g(self, x):
        return x*2

class G(F):
    def g(self, x):
        return x*3

class
