import weakref
# Test weakref.ref(x) and weakref.proxy(x)
#
# This test is not exhaustive, but it does test the most common cases.

# Test that ref(x) returns a weak reference to x, and that proxy(x)
# returns a weak reference to x that also has x's type.

class C(object):
    pass

class D(object):
    def __init__(self, arg):
        self.arg = arg

class E(D):
    pass

def f():
    pass

def g():
    pass

def h(x):
    pass

def i(x, y):
    pass

def j(x, y, z):
    pass

def k(x, y, z, t):
    pass

def l(x, y, z, t, u):
    pass

def m(x, y, z, t, u, v):
    pass

def n(x, y, z, t, u, v, w):
    pass

