import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

# Create a bunch of cyclical objects

class Foo:
    def __init__(self, i):
        self.i = i
        self.l = []

l = []
for i in range(100):
    foo = Foo(i)
    l.append(foo)

# Create a cycle
for i in range(0, len(l), 2):
    l[i].l.append(l[i+1])
    l[i+1].l.append(l[i])

# Create a bunch of non-cyclical objects
for i in range(100):
    Foo(i)

# Break the cycle
l = None

gc.collect()

# Now, make sure the cycle is really gone
for ob in gc.get_objects():
    if isinstance(ob, Foo):
        if ob.l:
            print(ob, ob.l)

# Try to break the cycle using weakrefs

l = []
for i in range(100):
    foo = Foo(i)
    l.append(weakref
