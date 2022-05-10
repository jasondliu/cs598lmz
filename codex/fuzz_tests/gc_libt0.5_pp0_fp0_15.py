import gc, weakref
from collections import defaultdict

from . import _core
from . import _util
from . import _graph
from . import _weakref_backports

_version = _core.__version__

__all__ = ['Node', 'NodeSeq', 'NodeMap', 'DirectedGraph', 'UndirectedGraph',
           'DiGraph', 'Graph', 'DiGraphView', 'GraphView', 'MultiGraph',
           'MultiDiGraph', 'MultiGraphView', 'MultiDiGraphView', 'is_weakref']

def is_weakref(ref):
    """
    Return True if *ref* is a weak reference to an object.
    """
    return isinstance(ref, weakref.ReferenceType)

class Node(object):
    """
    A node in a graph.

    A node can be part of multiple graphs.

    A node can hold arbitrary Python data.
    """

    __slots__ = ('_graph', '_id', '_attr')

    def __init__(self, graph, id, attr=None):
        self._graph = graph
       
