import _struct

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from . import memory_profiler

class Error(Exception):
  """Base class for exceptions in this module."""
  pass

class InvalidInput(Error):
  """Exception raised for errors in the input.

  Attributes:
    expression -- input expression in which the error occurred
    message -- explanation of the error
  """

  def __init__(self, expression, message):
    self.expression = expression
    self.message = message

class Graph:
  """Represents a graph.

  A graph is a list of its nodes and a list of its edges.
  """

  def __init__(self, nodes, edges):
    """Initializes the graph.

    Args:
      nodes: list of strings
      edges: list of tuples of strings
    """
    self.nodes = nodes
    self.edges = edges

class GraphReader:
  """Reads a graph from a file.

  The
