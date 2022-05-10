import gc, weakref
import json


class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = None
        if parent is not None:
            self.parent.children.append(self)

    def __repr__(self):
        return 'Node(%s)' % self.name

    def __iter__(self):
        return iter(self.children)

    def add_child(self, node):
        self.children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            for n in c.depth_first():
                yield n

    def breadth_first(self):
        yield self
        for c in self:
            for n in c.breadth_first():
                yield n


class FileNode(Node):
    def __init__(self, name, parent=None):
        super(FileNode, self).__init__(name, parent)
        self.data = {'created
