import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() for collectable objects with a __del__
# method.  Previously, such objects would be collected as soon as
# they became collectable (rather than being queued for later
# collection), when the collectable flag was checked.
#
# This test fails if it crashes with a fatal error.

# These objects should be collected, since the weakref callback is
# triggered by their __del__ method.
def callback(w):
    l.append(w)
class A(object):
    def __del__(self):
        print "A.__del__"
        wr = weakref.ref(self, callback)
a = A()
l = []
gc.collect()
assert len(l) == 1
l = []
a = None
gc.collect()
assert len(l) == 1

# These objects should be collected, since the weakref callback is
# triggered by the __del__ method of the object they reference.
class B(A):
    def __init__(self, ob):
        self.ob = ob
    def __del__(self):
        print "B.
