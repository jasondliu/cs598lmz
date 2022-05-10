import threading
threading.stack_size(268435456)

class Node(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.value = 0
        self.neighbor = []
        self.edge = []
        self.edge_value = []
        self.edge_to_neighbor = []
        self.edge_to_neighbor_value = []
        self.edge_to_neighbor_value_copy = []
        self.edge_to_neighbor_copy = []
        self.edge_value_copy = []
        self.edge_copy = []
        self.neighbor_copy = []
        self.neighbor_value_copy = []
        self.neighbor_value = []
        self.min_neighbor_value = []
        self.min_neighbor = []
        self.min_edge_value = []
        self.min_edge_to_neighbor = []
        self.min
