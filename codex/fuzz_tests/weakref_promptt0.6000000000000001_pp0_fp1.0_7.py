import weakref
# Test weakref.ref(self) for callable objects

class C(object):
    def __init__(self, val):
        self.val = val
    def __call__(self):
        return self.val
    def __hash__(self):
        return hash(self.val)

def f():
    print 'f()'

class D(object):
    def g(self):
        print 'D.g()'

def h():
    print 'h()'

for o in (C(1), f, D(), D.g, h):
    print o, ':',
    r = weakref.ref(o)
    print r(),
    print r() is o
    print 'callable:', callable(r())
