import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after the creation of a weak reference.
# The C code keeps strong references to these objects so they should
# never be collected.

a = {}; b = {}; c = {}
# References to the objects
ra = weakref.ref(a); rb = weakref.ref(b); rc = weakref.ref(c)
# Dictionary keeping strong references to the objects
d = {ra: 1, rb: 2, rc: 3}
print d.keys()

gc.collect()
assert ra() is a and rb() is b and rc() is c

# Now add a bound method of a random object to the cycle.
a.update({rb: 4})
assert rc() is c and ra() is a and rb() is b

# Check that the method can still be collected.
class Foo(object):
    def f(self):
        pass
m = Foo().f
mwr = weakref.ref(m)
del m
assert mwr() is None

# now clear the strong reference to m. This should cause m to be
# collected, and will thus
