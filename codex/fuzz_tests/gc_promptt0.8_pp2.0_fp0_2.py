import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
id(A)
a = A()
id(a)
# Requires to be able to use id() as a hash function and that we
# can hash all objects (incl. instances).
# We test this here, and then use the id() function freely in the
# tests below.
hash(A)
hash(a)
# This test fails when run standalone, if the garbage collector hasn't run for a
# while.  We therefore force a collection and check that the result is correct.
gc.collect()
id(A)
id(a)
del a
# We force another collection and check that the result is correct.
gc.collect()
id(A)
weakref.ref(A)
A = None
gc.collect()
# Now check that collect() returns the number of unreachable objects it found
gc.collect()
gc.collect()
class A:
    pass
gc.collect()
gc.collect()
a = A()
gc.collect()
gc.collect()
del a
gc.collect()
# Issue #4121: weakref.
