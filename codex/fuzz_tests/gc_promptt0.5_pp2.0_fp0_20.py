import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to objects with finalizers.
#
# This test is not very thorough; it only tests that gc.collect()
# correctly runs finalizers on objects that are otherwise uncollectible.
# It does not test that gc.collect() correctly runs finalizers on
# objects that are otherwise collectible.

class A:
    def __del__(self):
        print "del"

# Create a weakref to an object with a finalizer.
a = A()
r = weakref.ref(a)

# Remove the only reference to the object.
del a

# Run the garbage collector.
gc.collect()

# The object should still exist, because of the weakref.
print r() is not None

# Remove the weakref.
del r

# Run the garbage collector.
gc.collect()

# The object should have been collected.
