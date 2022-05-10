import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs
#
# This test is a bit tricky, because we want to test that gc.collect()
# really collects objects, but we don't want to rely on the exact
# details of the garbage collector's implementation.  So we create
# objects that are collectable, but we don't know exactly when they
# will be collected.  We use weakrefs to find out when they are
# collected.

# Create a bunch of objects, and make them weakly referencable.
# The objects are tuples, so they are collectable.

# Create a bunch of objects, and make them weakly referencable.
# The objects are tuples, so they are collectable.

class A:
    pass

def callback(ignore):
    global callback_ran
    callback_ran = 1

# Create a bunch of objects, and make them weakly referencable.
# The objects are tuples, so they are collectable.

a = A()
w = weakref.ref(a, callback)
del a
gc.collect()
assert callback_ran

a = A
