import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with uncollectable objects
# The objects list has a reference to the objects but
# the objects don't have references to each other or to
# the objects list.

class Foo:
    pass

objects = [Foo() for i in range(10)]

# We don't want objects to be garbage collected
# because then the test won't work.
# But they are just dangling references, so they will
# be garbage collected anyway.  To make sure that
# doesn't happen, we use a weakref.
r = weakref.ref(objects)

# In debug mode, Python holds objects alive until
# the next collection.  In non-debug mode, the
# objects are freed immediately.

if gc.isenabled():
    gc.collect(0)
    gc.collect(1)
    gc.collect(2)
    print(gc.garbage)
    assert len(gc.garbage) == 10
else:
    print('gc not enabled')

assert r() is objects
