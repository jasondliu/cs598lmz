import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs to old-style classes.

class A:
    pass

a = A()
a.x = a
w = weakref.ref(a)

del a
gc.collect()

# 'w' should still be alive.
print w() is None

# Now create a cycle with a new-style class.

class B(object):
    pass

b = B()
b.x = b
w = weakref.ref(b)

del b
gc.collect()

# 'w' should still be alive.
print w() is None
