import weakref
# Test weakref.ref() on a type.

class C(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'C(%r, %r)' % (self.x, self.y)

def f(C):
    return weakref.ref(C)

def g(C):
    return weakref.ref(C)

c = C(1, 2)
