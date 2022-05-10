import gc, weakref

class Node(object):
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []
        self.leaves = []
        self.branch_length = 0.0
        self.num_leaves = 0
        self.num_nodes = 0
        self.newick = None
        self.name = None
        self.support = None
        self.taxon = None
        self.id = None
        self.index = None
        self.distance_from_tip = None
        self.is_leaf = False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __iter__(self):
        """
        Iterate over the node and its children
        """
        yield self
        for child in self.children:
            for node in child:
                yield node

