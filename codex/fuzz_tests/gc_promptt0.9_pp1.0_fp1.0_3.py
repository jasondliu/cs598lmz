import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.  Note that it returns the number of objects
# collected and freed.


class C:

    def __init__(self):
        self.contains = [C(), C(), C()]


a = C()
b = C()
a.contains.append(b)
# Create a reference cycle.
b.contains.append(a)
print(gc.collect())
# Trigger collection of a and its contained objects.
del a
print(gc.collect())
# Ditto for b.
del b
print(gc.collect())
# We've "freed" all of the objects that contained a and b.  Their
# reference counts should go to zero.  But the container lists still
# exist.  We can go around the cycle once more freeing the empty
# container lists and then the cycle will be unreachable from the
# root set and should be collectale even though there are still no
# refcounts of zero.  We should be able to release a total of 12
# objects: 4 container instances and 8 contained instances.
print(gc.collect())
# Make sure that the cycle was in
