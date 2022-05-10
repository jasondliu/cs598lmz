import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after a bunch of cycles have been created and then are
# deleted.
# NB: we're not explicitly testing gc here as much as we're testing
# cycle-handling in general.  Using gc.collect() as a trigger is just a
# convenient way to force the cycles to be broken.

# Make a bunch of objects and put them into cycles.
class A:
    pass

for i in range(10000):
    a = A()
    a.cycle = a

# Keep a weakref to one of the objects.
ref = weakref.ref(a)
del a
# Only a few objects should be left around:
#
#	- 5 for the range() call
#	- 1 for the A class
#	- 1 for the ref() call
#
# (NB: ref() will create a frame object that's not directly reachable, and we
# don't count that in this calculation.)
#
# However, CPython's gc.get_objects() reports 1721 extra objects.  I have no
# idea why, but it's possible that they're objects temporarily being kept

