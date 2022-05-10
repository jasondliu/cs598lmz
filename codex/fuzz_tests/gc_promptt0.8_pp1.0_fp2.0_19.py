import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() called from a finalizer
class A:
    def __del__(self):
        weakref.ref(A())
    def __repr__(self):
        return "A"
a1 = A()
d = weakref.WeakValueDictionary({'a':a1})
# Force collection of a1, which should call a1.__del__ (which creates a temporary reference to a2)
# If this works, a2 should be collected when a1 is deallocated
a2 = a1
a1 = None
gc.collect()
# If a2 is collected, it should now be in the garbage collection list
assert not gc.collect()
print gc.garbage
