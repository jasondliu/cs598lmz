import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() fails with no collectable objects.
gc.collect()

# Test gc.collect() with collectable objects, and ensure
# no non-collectable objects.
w = weakref.ref(C())
gc.collect()
print "gc.collect() did not collect ", w()

# Test gc.collect() with non-collectable objects, and ensure
# no collectable objects.
gc.collect()
raises(TypeError, gc.collect)

# Test gc.collect() with one collectable and one non-collectable
# objects, and ensure all collectable objects are gone.
gc.collect()
print "gc.collect() collected ", w()
del w

# Test gc.collect() does not run finalizers.
gc.collect(2)
gc.collect(2)
print "gc.collect(2) did not run finalizers"

# Test gc.collect() runs finalizers.
gc.collect(1)
print "gc.collect(1) ran finalizers"

# test that variable-length objects do not prevent collections.
gc.collect()
