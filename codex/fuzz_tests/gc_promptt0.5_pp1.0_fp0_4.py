import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test checks that gc.collect() collects every object that is
# collectable.  It doesn't check that it collects only those objects.
#
# The test is a bit tricky to get right, because we want to check that
# gc.collect() collects every *collectable* object, but we don't want
# to create any uncollectable objects.  The basic approach is to
# create a bunch of gc-aware objects and check that all of them get
# collected.  However, we can't check this directly, because
# gc.is_tracked() only tells us about objects that *are* tracked, not
# objects that aren't.
#
# Instead, we use a pair of tricks.  First, we arrange for a
# "pseudo-finalizer" method to be called when each object is
# collected.  This method appends the object's id to a list.  Second,
# we arrange for a "real finalizer" to be called when the list is
# collected.  This finalizer checks that the list contains the ids of
# all the objects, and raises an
