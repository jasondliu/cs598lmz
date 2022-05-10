import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.garbage

# Create a bunch of objects and make them uncollectable
class A:
    pass

def f():
    a = A()
    a.b = A()
    a.b.a = a
    return a

a = f()
b = f()
a.b.b = b
b.b.b = a
del a, b

# Create some garbage
def g():
    for i in range(100):
        f()

g()

# Collect it
gc.collect()

# Check that the garbage is still there
assert gc.garbage

# Check that the garbage is collectable
gc.collect()
assert not gc.garbage

# Create some more garbage
g()

# Check that it's collectable
gc.collect()
assert not gc.garbage

# Create some more garbage
g()

# Check that it's not collectable
gc.collect()
assert gc.garbage

# Check that it's collectable
gc.collect()
assert not gc.garbage
