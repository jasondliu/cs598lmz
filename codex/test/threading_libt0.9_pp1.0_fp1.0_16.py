import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**7)

class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.used_edge_indices = set()
        self.node_count = self.get_node_count(edges)
        self.used_nodes_count = 0
        self.nodes = {}
        self.reverse_edges = []
        self.reverse_nodes = {}
        self.init_nodes(edges)
        self.reverse_graph = Graph(self.reverse_edges)

    def get_node_count(self, edges):
        node_count = 0
        for edge in edges:
            node_count = max(node_count, edge.first_node)
            node_count = max(node_count, edge.second_node)
        return node_count + 1

