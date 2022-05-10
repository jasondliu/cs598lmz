import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a class having a __del__ method.

class C(object):
    def __del__(self):
        pass

for i in xrange(5):
    C()

gc.collect()

# Test gc.collect() with a class having a weakrefable dictionary slot.

class D(object):
    def __init__(self, d):
        self.d = d

d2 = weakref.WeakValueDictionary()
d3 = weakref.WeakValueDictionary()

for i in xrange(5):
    d2[i] = D(d3)
    d3[i] = D(d2)

del d2, d3
gc.collect()

# Test gc.collect() with a class having a __del__ method that causes
# a reference cycle.

class E(object):
    def __del__(self):
        self.other = E()

e = E()
e.other = E()
e.other.other = e

del e
gc.collect()

# Test gc
