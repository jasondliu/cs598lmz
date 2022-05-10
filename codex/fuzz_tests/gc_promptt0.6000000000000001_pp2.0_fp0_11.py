import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in the face of cyclic trash that has a finalizer
# that does not call gc.collect().

# This test is a bit tricky to get right.  If you run it under a
# debug build, you'll see that the finalizer gets called in
# non-deterministic order.  Therefore we have to use a weakref
# callback to make sure that all finalizers have been called before
# proceeding.  We also have to use a separate list for each cycle,
# because it's possible that the callback will be invoked immediately
# after the object is appended to the list, in which case the list
# would be empty.  Finally, the test may fail if the test is run under
# a debug build and the finalizers are called in the wrong order.
#
# An alternative would be to use an explicit gc.collect() call in the
# finalizer, but that would be a lot slower (and would call
# gc.collect() recursively, which we don't currently support).

# On Mac OS X, the system malloc zone does not support finalization.
# Therefore, the weakref callback will
