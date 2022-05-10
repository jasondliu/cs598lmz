import weakref
# Test weakref.ref() on a class instance

class C(object):
    def __init__(self, a):
        self.a = a

    def __repr__(self):
        return 'C(%r)' % self.a

class D(object):
    def __init__(self, c):
        self.c = c

c = C(42)
d = D(c)
r = weakref.ref(c)

