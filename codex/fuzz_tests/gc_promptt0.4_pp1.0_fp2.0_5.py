import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Create a cycle
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return "A(%s)" % self.x

class B:
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "B(%s)" % self.a

# Create a cycle
a = A(42)
b = B(a)
a.b = b

# Verify that the cycle is collectable
assert gc.collect() == 2

# Create a weakref to the cycle
wr = weakref.ref(a)

# Verify that the weakref doesn't prevent collection
assert gc.collect() == 2
assert wr() is None

# Verify that the weakref doesn't prevent collection
a = A(42)
b = B(a)
a.b = b
wr = weakref.ref(a)
assert gc.collect() == 2
assert wr() is None

#
