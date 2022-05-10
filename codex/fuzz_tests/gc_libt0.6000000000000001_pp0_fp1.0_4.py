import gc, weakref
from collections import defaultdict

class Graph:
    def __init__(self, name):
        self.name = name
        self.nodes = weakref.WeakValueDictionary()
        self._node_cache = {}

    def add_node(self, name, **kwargs):
        if name in self._node_cache:
            return self._node_cache[name]

        node = Node(name, graph=self, **kwargs)
        self.nodes[name] = node
        self._node_cache[name] = node
        return node

    def add_edge(self, from_name, to_name, **kwargs):
        from_node = self.add_node(from_name)
        to_node = self.add_node(to_name)
        from_node.add_edge(to_node, **kwargs)

    def get_node(self, name):
        return self.nodes.get(name)

    def topological_sort(self):
        """
        Returns a list of nodes in topological order.
        """
