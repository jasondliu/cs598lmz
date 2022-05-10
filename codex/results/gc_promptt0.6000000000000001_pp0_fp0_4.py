import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable objects.  We should be able to
# collect everything but the cycle.

class A:
    pass

a = A()
a.b = A()
a.b.a = a

# Create a cycle with a finalizer; the finalizer will break the cycle.

class B:
    def __init__(self, b):
        self.b = b
    def __del__(self):
        self.b.b = None

b = B(B(b))

# Create a cycle with a weakref; the weakref will break the cycle.

c = A()
c.b = A()
c.b.a = c
c.b.wr = weakref.ref(c)

# Create a cycle with a weakref to a finalizer; the finalizer will
# break the weakref.

class C:
    def __init__(self, c):
        self.c = c
    def __del__(self):
        self.c.wr = None

d = C(C(d))
d.wr
