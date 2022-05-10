import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass

# Create weak references to one object.
w = weakref.ref(A())
w2 = weakref.ref(A())

# Create a weak reference to a collection of objects.
w3 = weakref.ref(set([A(), A(), A()]))

# Make sure the object is in a cyclic garbage collection
# state before we test its destructor.
del A

# Before Python knows it's in a cycle, its refcount should be 1.
assert sys.getrefcount(w()) == 2
assert sys.getrefcount(w2()) == 2
assert sys.getrefcount(w3()) == 2

gc.collect()

# After Python knows it's in a cycle, its refcount should be 2.
assert sys.getrefcount(w()) == 2
assert sys.getrefcount(w2()) == 2
assert sys.getrefcount(w3()) == 2

# But the gc still should call the weakref's __del__.
refs = [10]
def f():
    refs[0] -=
