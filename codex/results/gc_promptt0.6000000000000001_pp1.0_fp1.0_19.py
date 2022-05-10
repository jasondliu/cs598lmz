import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_objects()

# Create some objects to look at.
class A:
    def __init__(self):
        self.a = 1
        self.b = 'hello'
        self.c = [1, 2, 3]
    def __repr__(self):
        return "A(%r, %r, %r)" % (self.a, self.b, self.c)
class B:
    def __init__(self):
        self.a = A()
        self.b = A()
        self.c = A()
    def __repr__(self):
        return "B(%r, %r, %r)" % (self.a, self.b, self.c)

# Make some cycles.
a = A()
a.b = a
b = B()
b.a.b = b
b.b.b = b.a
b.c.b = b.a.c
b.a.c.append(b.b)

# Create some uncollectable objects.
a =
