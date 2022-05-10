import weakref
# Test weakref.ref() on an internal type

class D(object):
    pass

D.__init__(D, 1)
D.x = weakref.ref(D)
