import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collectable()
#
# This is a straightforward test to make sure gc.collectable()
# returns true for objects in the garbage with no references.

import gc
gc.set_debug(gc.DEBUG_COLLECTABLE)

l = []
for i in range(1000):
    obj = {}
    obj['foo'] = 'bar'
    l.append(obj)

class recursive:

    def __init__(self, num):
        self.num = num
        self.next1 = None
        self.next2 = None
        self.next3 = None

# create a recursive list
nodes = [recursive(i) for i in range(100)]
for i in range(len(nodes)):
    if i:
        nodes[i].next1 = nodes[i-1]
        nodes[i].next2 = nodes[i-1]
        nodes[i].next3 = nodes[i-1]

# remove them from the list and make sure they are collectable
for node in nodes:
    node.next1 = None
    node.
