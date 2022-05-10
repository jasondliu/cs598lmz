import gc, weakref

from . import test_graph
from .test_graph import TestGraph

from .. import graph, graph_types, util, GraphError
from ..graph import Graph, GraphType, Node, Edge


class TestGraphUtility(TestGraph):
    def test_get_dangling_nodes(self):
        self.graph.add_node(0, 1)
        self.graph.add_node(0, 2)
        self.graph.add_node(0, 3)
        self.graph.add_edge(0, 1, 2, 'a')
        self.graph.add_edge(0, 2, 3, 'b')
        dangling = self.graph.get_dangling_nodes()
        self.assertEqual(len(dangling), 2)
        self.assertTrue(1 in dangling)
        self.assertTrue(3 in dangling)

    def test_get_degree(self):
        self.graph.add_node(0, 1)
        self.graph.add_node(0, 2)
        self.graph.add_node(0,
