import weakref

import numpy as np

from .base import Node
from .core import Array, ArrayArg

class Graph(object):
    """Node graph.

    Parameters
    ----------
    node_list : list
        List of nodes.

    Attributes
    ----------
    node_list : list
        List of nodes.
    node_dict : dict
        Dictionary mapping node IDs to node instances.
    """
    def __init__(self, node_list):
        self.node_list = node_list
        self._init_node_dict()

    def _init_node_dict(self):
        self.node_dict = dict()
        for node in self.node_list:
            self.node_dict[node.id] = node

    def toposort(self):
        """Topologically sort nodes in the graph.

        Returns
        -------
        list
            Sorted list of nodes.
        """
        # TODO: make this more efficient
        # TODO: make this more robust
        # TODO: make this less brittle
        # TODO: make this
