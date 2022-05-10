import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() when there are weakrefs to uncollectable objects
# (e.g. instances of classes with __del__ methods).
#
# This test is a bit tricky because we need to create a cycle that
# only involves uncollectable objects, and then break the cycle.  If
# we create the cycle using collectable objects, the cycle will be
# collected immediately and we won't exercise the code we're trying
# to test.
#
# We create the cycle using instances of a class that has a __del__
# method.  This makes the instances uncollectable.  Then we create a
# weakref to one of the instances.  This won't prevent the instances
# from being collected, but it will cause the weakref object to be
# placed on the list of weakrefs to be notified when the instances
# are collected.  Then we break the cycle.  Now the instances are
# collectable, and will be collected by the next call to gc.collect().
# But first, the weakrefs on the list of weakrefs to be notified will
# be processed, and the callback functions will be called.
#

