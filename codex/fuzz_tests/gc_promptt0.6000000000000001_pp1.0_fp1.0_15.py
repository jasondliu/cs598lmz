import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Create a cyclic list of a few objects.  Then delete one of the objects,
# and make sure the cyclic list gets collected.
#
a = []
b = [a]
a.append(b)
del a
#
# The list b should still be alive, but the list a should be gone.
#
gc.collect()
print len(gc.get_objects())
#
# Now create a cyclic list of objects, where one of the objects is a
# class instance.  If the class instance is not correctly marked as
# GC-aware, the list will not be collected.  The list should be
# collected by the next call to collect().
#
class A:
    pass
a = []
b = [a]
a.append(b)
a.append(A())
del a
#
# The list b should still be alive, but the list a should be gone.
#
gc.collect()
print len(gc.get_objects())
#
# Here is a variant of the above test.  If the class instance is not
# correctly marked as
