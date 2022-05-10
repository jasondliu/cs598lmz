import weakref
# Test weakref.ref() with a class that has a __del__ method.

class C:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        print "deleting", self.x

def f(x):
    print "f", x

def g(x):
    print "g", x

def h(x):
    print "h", x

def check(r, expected):
    if r() != expected:
        raise RuntimeError, "expected %r, got %r" % (expected, r())

c = C(1)
r = weakref.ref(c, f)
check(r, c)

c = C(2)
r = weakref.ref(c, g)
check(r, c)

c = C(3)
r = weakref.ref(c, h)
check(r, c)

c = C(4)
r = weakref.ref(c, None)
check(r, c)

c = C(5)
r = weak
