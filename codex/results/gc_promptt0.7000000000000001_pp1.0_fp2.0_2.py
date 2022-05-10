import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect on weakrefs.

# Create a weakref to an object, then create a cycle with it.

class A(object):
    pass

a = A()
b = A()
b.d = a
a.d = b

# Create a weak reference to a.

w = weakref.ref(a)

# Now delete everything.

del a, b
gc.collect()

# This used to trigger a fatal error.  Now the weak reference
# should be dead, and collecting it should have no effect.

print w() is None

w = weakref.ref(b)
del b
gc.collect()
print w() is None


class C(object):
    def __del__(self):
        pass

c = C()
w = weakref.ref(c)

del c
gc.collect()
print w() is None

# Exercise the weakref callbacks.
# The callbacks should be called at most once, but no sooner than the
# weakref is created.

class D(object):
    pass

class E
