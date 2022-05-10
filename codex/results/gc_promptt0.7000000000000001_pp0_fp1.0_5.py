import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by watching the finalization of weakrefs
# in a cyclic data structure.

class Node:
    def __init__(self, next = None):
        self.next = next

# Build a data structure that looks like:
#    root -> Node -> Node -> ...
#                  ^       |
#                  |       |
#                weakref   |
#                        self.next

# Create an initial cycle with no weakrefs
root = Node()
n = root
for i in range(10):
    n.next = Node(n.next)
    n = n.next
# Weakref the last Node
w = weakref.ref(n)

# Clear the reference to the root.  Since there are no weakrefs
# in the cycle yet, gc doesn't collect it.
root = None
gc.collect()
assert w() is n

# Now add a weakref to the first Node in the cycle
root = Node(n)
n.next = root
gc.collect()
assert w() is n

# Now add a weakref to the last Node in the
