import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky.  We have to make sure that the objects
# we create are actually collected, and that the weakrefs are cleared
# as a result.  We can't just check that the weakrefs are cleared,
# because they may be cleared by other collections.  So we have to
# make sure that the objects are collected, and then check that the
# weakrefs are cleared.
#
# We do this by creating a bunch of objects, and then creating a bunch
# of weakrefs to them.  Then we delete the objects, and collect.  Then
# we check that the weakrefs are cleared.  Then we create a bunch of
# new objects, and check that the weakrefs are not cleared.  Then we
# delete the objects, collect, and check that the weakrefs are cleared.
#
# Note that we can't use unittest.TestCase, because we need to be able
# to run the tests in a subinterpreter.

# Create a bunch of objects, and a bunch of weakrefs to them.
objects = []
weakrefs
