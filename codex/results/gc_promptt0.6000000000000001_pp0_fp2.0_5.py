import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
# Create a cycle with two lists.
lst = [1, 2, 3]
lst.append(lst)
lst2 = [lst, lst]
lst2.append(lst2)
# Create a cycle with a dict.
dct = {}
dct[1] = dct
# Create a cycle with an object.
class A:
    def __init__(self):
        self.other = self
a = A()
# Create a cycle with a weakref.
wr = weakref.ref(lst)
# Check that all objects are collectable.
for obj in (lst, lst2, dct, a, wr):
    if not gc.is_collectable(obj):
        raise TestFailed, '%s is not collectable' % type(obj)
# Check that all objects are tracked.
for obj in (lst, lst2, dct, a):
    if not gc.is_tracked(obj):
        raise TestFailed, '%s is not tracked' %
