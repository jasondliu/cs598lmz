import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.
#
# Some objects are left uncollectable to support __del__ methods,
# because we don't know whether the __del__ method will make the object
# collectable again.  This test ensures that those objects are collected
# when collect() is called.

class C:
    def __del__(self):
        pass

class D:
    pass

class E(D):
    def __del__(self):
        pass

def check(lst, n):
    if lst != n * [None]:
        raise ValueError, 'unexpected list: ' + repr(lst)

# Create an uncollectable list
check(gc.collect(), 0)
gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
l = []
l.append(l)
# Create a list of uncollectable objects
check(gc.collect(), 0)
ll = [C() for i in range(10)]
ll.append(ll)
check(gc.collect(), 0)
# Create a cycle with an uncollectable list
check(
