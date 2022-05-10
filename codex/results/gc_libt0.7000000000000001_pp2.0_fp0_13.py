import gc, weakref

gc.disable()

class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
        self._height = 0

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

    def get_level(self):
        return self._height

    def update_height(self):
        self._height = self.parent.update_height() + 1 if self.parent is not None else 0
        return self._height


root = Node('parent')
c1 = Node('child')
c2 = Node('child')

