import weakref
# Test weakref.ref(x) == weakref.ref(x) for various x

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(object):
    pass

def f():
    pass

class E(object):
    def g(self):
        pass

class F(object):
    def __init__(self, x):
        self.x = x

x1 = A()
x2 = B()
x3 = C()
x4 = D()
x5 = f
x6 = E()
x7 = E()
x8 = F(1)
x9 = F(2)

def check_eq(x, y):
    # The following should always return true
    assert weakref.ref(x) == weakref.ref(x)
    assert weakref.ref(x) is weakref.ref(x)
    assert not (weakref.ref(x) != weakref.ref(x))
