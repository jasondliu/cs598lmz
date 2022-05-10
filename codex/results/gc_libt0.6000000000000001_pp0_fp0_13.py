import gc, weakref

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = []
        self.node_neighbors = {}
        self.edge_cost = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.nodes.append(node)
            if node not in self.node_neighbors:
                self.node_neighbors[node] = []

    def add_edge(self, fromnode, tonode, cost=0):
        if fromnode == tonode:
            raise ValueError('fromnode == tonode')
        if fromnode not in self.nodes:
            self.nodes.append(fromnode)
        if tonode not in self.nodes:
            self.nodes.append(tonode)
        self.edges.append((fromnode, tonode))
        self.edge_cost[(fromnode, tonode)] = cost
        if tonode not in self.node_neighbors
