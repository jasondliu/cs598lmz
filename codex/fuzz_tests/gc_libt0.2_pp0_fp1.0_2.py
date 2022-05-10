import gc, weakref

class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
    def add_child(self, child):
        self.children.append(child)
        child.parent = self

root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)

del root
gc.collect()
print(c1.parent)

"""
    The weakref module provides tools for tracking objects without creating
    references that prevent the garbage collector from reclaiming the memory
    they occupy.
"""

a_set =
