import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky, because we want to test that gc.collect()
# collects all unreachable objects.  But we don't want to rely on
# gc.collect() finding *all* unreachable objects, because the set of
# reachable objects can include objects reachable from the environment
# of the Python interpreter, and we can't know what those are.  So we
# create a bunch of objects, and then create a second bunch of objects
# that depend on the first bunch.  The second bunch is intentionally
# much larger than the first, so that the first bunch is a small
# fraction of the total number of objects reachable from the
# interpreter.  We then delete references to the first bunch, and
# invoke gc.collect().  If the first bunch is not collected, then the
# memory consumed by the first bunch is a non-trivial fraction of the
# total memory consumed by the test, and we report the test as having
# failed.
#
# Note that we can't usefully test the return value of gc.collect(),
# because it will be non-zero if any
