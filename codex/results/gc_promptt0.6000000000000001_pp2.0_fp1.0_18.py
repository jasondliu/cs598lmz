import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.
# Create a cycle, and make sure the callback gets called.

class A:
    def __init__(self):
        self.b = B(self)

class B:
    def __init__(self, a):
        self.a = a

def callback(wr):
    print "callback"
    raise RuntimeError

a = A()
# We need to hold a reference to the weakref object, so the
# callback gets called.
wr = weakref.ref(a, callback)
a = None
gc.collect()
print gc.garbage
