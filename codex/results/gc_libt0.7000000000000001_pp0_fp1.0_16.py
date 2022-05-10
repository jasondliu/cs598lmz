import gc, weakref
import numpy as np
import torch
import torch.autograd as autograd

from consts import *
from graph_utils import *

#TODO: 1. add support for multiple layers and multiple groups 2. support multiple edges between two nodes
class Graph(object):

    def __init__(self, n_nodes, layers=1,
            edges=None, adj_list=None, adj_dict=None,
            is_directed=False, is_cyclic=False,
            all_nodes=None, all_edges=None,
            node_dim=None, edge_dim=None,
            edge_types=None, edge_stypes=None,
            edge_index=None, edge_index2=None,
            edge_stypes2=None, edge_stypes3=None,
            edge_type_idx=None, edge_type_idx2=None,
            edge_type_idx3=None, edge_types2=None,
            edge_types3=None, edges2=None, edges3=None,
           
