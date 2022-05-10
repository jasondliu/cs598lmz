import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback.

# Create a cycle, and register a weakref callback on one of the objects.
def callback(w):
    print "callback", w

class A:
    pass

a = A()
b = A()
a.b = b
b.a = a

wr = weakref.ref(a, callback)

# Collecting the cycle should invoke the callback.
print "Collecting"
gc.collect()
print "done"

# Collecting again should not invoke the callback.
print "Collecting again"
gc.collect()
print "done"

# After breaking the cycle, collecting should not invoke the callback.
print "Breaking cycle"
del a, b
gc.collect()
print "done"

# After breaking the cycle, collecting again should not invoke the callback.
print "Collecting again"
gc.collect()
print "done"
