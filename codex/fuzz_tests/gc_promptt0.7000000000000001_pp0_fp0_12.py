import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, n):
        self.n = n

class Bar:
    def __init__(self, n):
        self.n = n

def f(a):
    print str(a), gc.get_referents(a)

def dump(a):
    for x in gc.get_referrers(a):
        f(x)

# A new list with one item, a, will be allocated.
a = Foo(1)
a.a = a
f(a)
print

# The list will be deallocated, but a won't because it
# has a refcount of 2 (one from a, one from the list).
a = None
gc.collect()
print

# Now a's refcount is 1 (from globals()).  It will be
# deallocated eventually, but we have to force it.
gc.collect()
print

# The list is deallocated, and a is now also deallocated.
a = []
gc.collect()
print

