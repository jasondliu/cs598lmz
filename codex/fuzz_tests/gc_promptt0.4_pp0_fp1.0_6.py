import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
#
# This test is a bit tricky, because the weakrefs are not
# necessarily destroyed immediately when the referent is
# destroyed.  So we have to use a loop to make sure that
# the weakrefs are destroyed.

# Create a bunch of objects and a bunch of weakrefs to them

# The objects are a list of tuples, where each tuple contains
# a bunch of objects.  The idea is to make it hard for the
# garbage collector to know that the tuple is dead, because
# it is referenced from a list.

# The weakrefs are stored in a list, so that they are not
# destroyed immediately.

# The objects are also stored in a list, so that they are not
# destroyed immediately.  (This is not strictly necessary, but
# it makes the test more realistic.)

# The test is successful if the weakrefs are destroyed, and
# if the objects are destroyed.

# Create a bunch of objects, and a bunch of weakrefs to them.

# The objects are a list of tuples, where each tuple contains
# a
