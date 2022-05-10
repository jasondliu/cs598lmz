import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakrefs.

# This test is very simple, but it is the only test of gc.collect() with
# weakrefs.  I don't want to add more tests here, because the tests for
# weakrefs themselves already test everything.

# If a weakref is not collected, the object it refers to may not be
# collected either.  In that case, the object should not be reported.

class Klass:
    pass

def f():
    return Klass()

a = Klass()
b = Klass()

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)

del a, b

collectable = gc.collect()
collected = gc.collect()

assert collectable == 2
assert collected == 0

# Now create a weak reference to a new object.  The old object should be
# collected, but not the new one.

c = f()
c_wr = weakref.ref(c)

del c

collectable = gc.collect()
collected = g
