import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when an object with a weakref is being tracked
# by the garbage collector.

class Foo:
    def __init__(self, k):
        self.k = k
    def __del__(self):
        print "collecting", self.k

def f():
    x = Foo(1)
    y = Foo(2)
    z = weakref.ref(y)
    x.a = x
    x.b = y
    y.a = x
    y.b = y
    del x, y

# This used to raise an exception because of a bug in the garbage
# collector.  Now it shouldn't.
print "collecting..."
f()
gc.collect()

# Now check that the garbage collector is still working properly
# after collecting such an object.

print "collecting again..."
f()
gc.collect()
print "done"
