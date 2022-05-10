import types
types.MethodType(lambda self: None, None, Dummy)

# Test for SF bug #1424246
class C:
    "Test for classic classes"
    pass

class D(C):
    "Test for new style classes"
    pass

def f(self):
    "Test for instance methods"
    pass

def g(cls):
    "Test for class methods"
    pass

def h(self, x, y):
    "Test for instance methods with arguments"
    pass

def i(cls, x, y):
    "Test for class methods with arguments"
    pass

c = C()
d = D()

c.f = types.MethodType(f, c)
c.g = types.MethodType(g, c, C)
c.h = types.MethodType(h, c)
c.i = types.MethodType(i, c, C)

d.f = types.MethodType(f, d)
d.g = types.MethodType(g, d, D)
d.h = types.Method
