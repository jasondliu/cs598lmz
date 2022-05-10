import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a cyclic object graph

# First, create a cyclic object graph.
class Node:
    def __init__(self, name):
        self.name = name
        self.others = []
    def set_others(self, others):
        self.others = others
    def __repr__(self):
        return 'Node(%r)' % self.name

a = Node('a')
b = Node('b')
c = Node('c')
a.set_others([b, c])
b.set_others([c, a])
c.set_others([a, b])

# Now, create a weakref to a.
a_ref = weakref.ref(a)

# Now, clear all references to a, b and c.
a = b = c = None

# Now, check that we can still access the weakref to a.
assert a_ref() is not None

# Now, do a collect.
gc.collect()

# Now, check that we can still access the weakref to a.

