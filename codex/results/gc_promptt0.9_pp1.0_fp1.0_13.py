import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs and with cyclic GC-tracked objects.

import sys, gc

# Cyclic objects.
class C:
    def __init__(self, n):
        self.n = n
        self.loop = [self]

class T(C):
    pass


def test_collect(n):
    print 'testing', n
    # Create a cyclic object with a weakref pointing to it.
    a = T(n)
    # Create a second cycle.
    x = T(n)
    x.loop.append(x)
    # "a" starts off alive, and "b" is a dead object.  If the weakref is
    # called when "a" is collected, b will spring to life and then be
    # collected again.  The cycle x is to keep b from being considered
    # collectable by the cycle detector.
    b = weakref.ref(a)
    y = C(n)
    y.loop = [y, x]
    del a, x
    wr = weakref.ref(y)

