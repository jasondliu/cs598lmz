import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs on a built-in type.

class MyTuple(tuple):
    pass

class MyObject:
    def __init__(self):
        self.t = MyTuple((self, 1))

o = MyObject()

# Create a reference cycle.
o.t[0].t = o.t

# Create a weak reference to o.
r = weakref.ref(o)

# Break the reference cycle.
o = None

# The weak reference can still be used.
print(r().t)

# Collect.
gc.collect()

# The weak reference no longer exists.
print(r())
