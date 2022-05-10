import types
# Test types.FunctionType
def f(a, b, c=None):
    print a, b, c
assert type(f) is types.FunctionType

# Test class type
class A(object):
    def __init__(self, a, b, c=None):
        self.a = a
        self.b = b
        self.c = c

a = A(1, 2, 3)
assert type(a) is A
assert type(a.a) is int
assert type(a.b) is int
assert type(a.c) is int

try:
    c = type(a)(1, 2, 3)
    assert False
except TypeError:
    pass

# Test __init__ method
class B(object):
    def __init__(self):
        pass
b = B()

# Test __new__ method
class C(object):
    def __new__(cls):
        return object.__new__(cls)
c = C()
assert type(c) is C

# Test object attribute
class D(object):
   
