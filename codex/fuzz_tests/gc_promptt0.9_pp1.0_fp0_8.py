import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref
#
# Verify that we are collecting regular objects

a = []
a.append(a)

wr = weakref.ref(a)

# Clear a reference to a
a = None
del a
#
# We just freed a, weakref to a should still be valid
assert wr() is not None
#
# Run a full collection...
gc.collect()

#
# We now should actually have destroyed the object pointed by weakref
assert wr() is None

#
# Test gc.garbage
#
a = []
a.append(a)

a = None
del a

#
# Run a full collection...
gc.collect()

#
# Garbage list should be populated by our circular list
assert a in gc.garbage

gc.set_debug(0)
#
# Test the __del__ method on a cyclic structure

del_flag = []

class A:
    def __del__(self):
        del_flag.append(None)

a = A()
a.self = a

