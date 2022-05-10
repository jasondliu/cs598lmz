import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref callbacks
# Note that gc.collect() is called automatically between tests
# This tests if the callback is called for objects collected by gc.collect()
# and if the objects are really collected.

class A:
    def __del__(self):
        print "A.__del__()"

# Disable garbage collection of A instances
A._hash_C_A = A.__hash__
def __hash__(self):
    return self._hash_C_A()
A.__hash__ = __hash__

def callback(wr):
    print "callback(%r)" % (wr,)

# Test with a callback
a = A()
wr = weakref.ref(a, callback)
del a
gc.collect()
print "Callback result:", wr()

# Test without a callback
a = A()
wr = weakref.ref(a)
del a
gc.collect()
print "No callback result:", wr()

# Test with a different callback
a = A()
wr = weakref.ref(a, callback)
del a

