import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.
#
# This time create a reference cycle.

class A:
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        return "A(%s)" % self.i

class B:
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        return "B(%s)" % self.i

class C:
    def __init__(self, i):
        self.i = i
    def __repr__(self):
        return "C(%s)" % self.i

# Create a cycle.
def callback(ref):
    print 'callback', ref()
a = A(0)
b = B(a)
c = C(b)
a.b = b
a.c = c

# Break the cycle.
a.b = None
a.c = None

# Check that the cycle is gone.
#print "collecting"
#gc.collect()

#
