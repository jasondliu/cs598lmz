import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() without garbage.
# This invokes callbacks, so it used to be buggy.
gc.collect()

# Test gc.collect() with a callback, some garbage, and a finalizer.
# Again, this used to be buggy.

def callback(count, thresholds):
    print 'garbage collecting'
    print count, thresholds

def finalize(arg):
    print "Calling finalizer", arg

gc.enable()
gc.set_debug(gc.DEBUG_STATS)
gc.set_threshold(1, 2, 3)
gc.set_callback(callback)

# Create a cycle with a finalizer
class Foo:
    def __init__(self, x):
        self.x = x
    def __del__(self):
        finalize(self.x)

f = Foo(42)
g = Foo(f)
f.x = g

# Create some garbage
for i in range(100):
    gc.collect()
    # Force creation of some garbage.
    [x for x in range(10000)]

print "done
