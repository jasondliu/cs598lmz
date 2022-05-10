import gc, weakref

from nose.tools import assert_equal

from numpy.testing import assert_array_equal, assert_array_almost_equal
from numpy.testing.decorators import skipif

# Local imports
from networkx import convert_matrix, NetworkXError
from networkx.utils import Index, is_string_like
from networkx.convert_matrix import to_numpy_matrix, from_numpy_matrix
from networkx.convert_matrix import to_scipy_sparse_matrix, from_scipy_sparse_matrix
from networkx.convert_matrix import to_dict_of_dicts, from_dict_of_dicts
from networkx.generators.classic import empty_graph, path_graph, complete_graph
from networkx.convert import to_edgelist
import networkx as nx

class TestConvert(object):
    """Unit tests for convert functions."""

    def test_to_numpy_array(self):
        G=nx.path_graph(4)
        A=
