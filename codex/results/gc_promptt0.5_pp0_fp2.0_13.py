import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This is a test of the gc module.  The purpose is to ensure that
# collect() works.  The strategy is to create a bunch of objects
# and then collect() and verify that they have been collected.
# The objects are created in such a way that they will be collected.
#
# The test has two phases:
#
#   1. Create a bunch of objects that are collectable.
#   2. Call gc.collect() and verify that they have been collected.
#
# The details are a bit more complex, because we want to verify that
# collect() works even in the presence of cycles and we want to verify
# that gc.garbage contains the objects that were in cycles.
#
# To do this, we create a bunch of objects that are not in cycles and
# verify that collect() collects them.  Then we create a bunch of
# objects that are in cycles, and verify that collect() collects them
# and that the resulting garbage contains the objects that were in the
# cycles.
#
# The objects are tuples of the form
#
#   (obj, hash(
