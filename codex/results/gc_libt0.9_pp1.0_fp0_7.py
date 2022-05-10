import gc, weakref
from math import inf
from operator import itemgetter
import multiprocessing, multiprocessing.managers
from itertools import repeat
import pandas as pd

from retrofuturiste.dijkstra import ShortestPathFinder

def eulerian_path(graph: Mapping[Vertex, Iterable[Tuple[Vertex, Weight]]]):
    """
    Find the Eulerian path in a multigraph.

    The graph *must* be connected.
    If it is not, this will most likely return an error
    as it will not be able to find a cycle in the graph.

    P.S.: in some corner cases this is not the Eulerian cycle,
        but I see no problem until someone shows me the corner case.
    P.P.S.: the cycle is entirely constructed from the lexicographical order of the edges.
        In other words, the search always tries to find a lexicographically minimal edge
        from the current vertex.

    :param graph:
        a graph as a mapping from vertices to iterables of (*neighbour*, *weight*) pairs
