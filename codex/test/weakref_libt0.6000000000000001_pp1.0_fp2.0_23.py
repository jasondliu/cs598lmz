import weakref


def _get_target(target):
    if isinstance(target, weakref.ProxyType):
        return target
    return weakref.proxy(target)


def _get_targets(targets):
    return [_get_target(t) for t in targets]


class Node:
    def __init__(self, name, targets=None):
        self.name = name
        self.targets = targets or []
        self.targets = _get_targets(self.targets)
        self.out_degree = 0
        self.in_degree = 0
        self.in_nodes = []
        self.out_nodes = []

    def __repr__(self):
        return "<Node: %s>" % self.name


class Graph:
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.add_nodes(nodes)
        self.add_edges(edges)


