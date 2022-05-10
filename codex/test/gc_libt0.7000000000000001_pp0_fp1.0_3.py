import gc, weakref

class Node(object):
    def __init__(self, data):
        self.data = data
        self._parent = None
        self.children = []
        self._depth = 0
        self._height = 0
        self._nb_descendants = 1

    def add_child(self, node):
        assert isinstance(node, Node)
        self.children.append(node)

        node._parent = weakref.ref(self)
        node._depth = self._depth + 1
        self._height = max(self._height, node._height + 1)
        self._nb_descendants += node._nb_descendants

    @property
    def parent(self):
        return self._parent() if self._parent is not None else None

    @property
    def depth(self):
        return self._depth

    @property
    def height(self):
        return self._height

    @property
    def nb_descendants(self):
        return self._nb_descendants

