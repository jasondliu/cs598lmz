import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable() with a weakref to an object of a custom type
# The object must be uncollectable when the weakref is alive,
# but must be collectable when the weakref is dead.
class A:
    pass
def kill(wr, n):
    # The weakref should be alive at this point.
    assert wr() is not None
    print(gc.collectable())
    del globals()['n%d' % n]
    print(gc.collectable())
a = A()
wr = weakref.ref(a, kill)
globals()['n%d' % id(a)] = a
# The weakref should be alive at this point.
assert wr() is not None
print(gc.collectable())
del a
print(gc.collectable())
# The weakref should be dead at this point.
assert wr() is None
print(gc.collectable())
try:
    import threading
except ImportError:
    pass
else:
    # Issue #2657: a weakref to a dead object should not be callable
    class A:
       
