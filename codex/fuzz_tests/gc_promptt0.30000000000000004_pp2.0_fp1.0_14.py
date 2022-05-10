import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is a bit tricky.  The goal is to test that gc.collect()
# collects everything that's collectable.  But it's hard to tell what
# "collectable" means, because the garbage collector is free to collect
# objects that are reachable but not referenced (e.g. if they're
# referenced only by a __del__ method or a weakref).
#
# The strategy here is to create a bunch of objects, and then delete
# every reference to them.  If the objects are still alive after
# gc.collect(), then they must be reachable in some way that the
# collector doesn't understand.  The objects are arranged into a
# hierarchy, so that we can test that the collector understands
# circular references.
#
# Note that we can't actually verify that no objects are collected,
# because the collector is free to collect objects that are part of
# the test framework.  The goal is to make sure it doesn't collect any
# objects that we specifically arrange for it not to collect.

# Create a bunch of objects, and arrange them into a hierarchy.  The
#
