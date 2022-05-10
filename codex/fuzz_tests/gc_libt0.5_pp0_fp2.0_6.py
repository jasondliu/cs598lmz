import gc, weakref
from collections import defaultdict

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def __repr__(self):
        return 'Node({0!r:s})'.format(self.value)

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.node_map = {}

    def add_node(self, value):
        node = Node(value)
        self.nodes.append(node)
        self.node_map[value] = node
        return node

    def get_node(self, value):
        return self.node_map.get(value)

    def add_edge(self, value1, value2):
        if value1 == value2:
            raise ValueError('Cannot create cycle edge')
        node1 = self.get_node(value1)
