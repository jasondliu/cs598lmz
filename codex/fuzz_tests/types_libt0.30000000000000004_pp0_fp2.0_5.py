import types
types.MethodType(lambda self: 42, None)

# Test __new__
class A(object):
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self, x):
        self.x = x

A(42)

# Test __init__
class B(object):
    def __init__(self, x):
        self.x = x

B(42)

# Test __del__
class C(object):
    def __del__(self):
        pass

C()

# Test __getattribute__
class D(object):
    def __getattribute__(self, name):
        return 42

D().x

# Test __getattr__
class E(object):
    def __getattr__(self, name):
        return 42

E().x

# Test __setattr__
class F(object):
    def __setattr__(self, name, value):
        self.__dict__[name] = value

F().x = 42
