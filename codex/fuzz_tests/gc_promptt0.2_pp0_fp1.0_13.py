import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# The following test is a bit tricky.  We create a bunch of objects,
# and then we collect them.  However, we also create a bunch of
# weakrefs to those objects.  The weakrefs are stored in a list, so
# they are kept alive by the garbage collector.  However, the objects
# they refer to are not kept alive by the garbage collector, so the
# weakrefs should be set to None when the objects are collected.
#
# We then call gc.collect() and check that the weakrefs are indeed set
# to None.  If they are not, then the objects are not being collected.
#
# This test is a bit tricky because the objects are collected before
# the test starts.  So we have to create the weakrefs *before* we
# create the objects.  This is why the test is a bit convoluted.

# Create a bunch of weakrefs.  They will be set to None when the
# objects they refer to are collected.
w = [weakref.ref(None) for i in range(100)]

# Create a bunch of
