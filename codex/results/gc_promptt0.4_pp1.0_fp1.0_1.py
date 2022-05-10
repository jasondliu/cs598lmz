import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
gc.collect()

# Test weakref
class Foo:
    pass

a = Foo()
b = Foo()

c = a

# Create a weak reference to a
w = weakref.ref(a)

# Remove all references to a
del a

# Create a reference cycle
a = Foo()
a.b = b
b.a = a

# Create a weak reference to a
w = weakref.ref(a)

# Remove all references to a
del a

# Test gc.get_referrers()
a = Foo()
b = Foo()

c = a

# Create a reference cycle
a.b = b
b.a = a

# Test gc.get_referrers()
gc.get_referrers(a)
gc.get_referrers(b)

# Test gc.get_referrers() with a weakref
a = Foo()
b = Foo()

c = a

# Create a reference cycle
a.b = b
b.a
