import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on weakrefs with callbacks.

def callback(wr, selfref=ref(self)):
    self = selfref()
    try:
        # Test whether the callback is invoked inside
        # gc.collect().  Working around Python issue #1776040.
        inside_collect = gc.collect() >= 0
    except RuntimeError:
        # If that's broken, assume we are inside gc.collect().
        inside_collect = True
    self.do_collect = self.do_collect + 1
    self.inside_collect = self.inside_collect + inside_collect

self = C()
self.do_collect = 0
self.inside_collect = 0
cbacks = []
# Create several callbacks, saving the wrappers for the callback early in
# the weakref list and later in the list.  Invariant: callback[2*i+1]
# will expire first.
for i in range(10):
    gr = self.grow(10)
    wr1 = weakref.ref(gr, callback)
    wr2 = weakref.ref(gr,
