import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

# Create a few objects and some weakrefs to them.

class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d[1] = a
d[2] = a
d[3] = a

del a

# The dictionary should stay alive until its last reference is removed.
check(d)

# Once the dictionary is gone, its objects should be collectable.
del d
collect()
assert gc.collect() == 3

# Without the fixes for bug #977828 and bug #362270, the following
# would fail with a RuntimeError:

#        gc: collectable <A 0x0092B7F0>
#        gc: collectable <A 0x0092B7F0>
#        gc: collectable <A 0x0092B7F0>
#        gc: collectable <dict 0x0092B818>
#        gc: collectable <dict 0x0092B818>
#        gc: collectable <dict
