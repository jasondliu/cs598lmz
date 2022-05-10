import weakref
# Test weakref.ref to save memory
x = "String"
x_wr = weakref.ref(x)
print(x_wr())
print(type(x_wr()))
# After the object is removed, [] is returned
x = 0
print(x_wr())

class Node:
    def __init__(self, data):
        self.data = data
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.data)

    # Property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

root = Node('parent')
c1 = Node('child')
root.add_child(c1)
