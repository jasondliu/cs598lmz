import gc, weakref
import numpy as np

from utils import xrange, unique
from itertools import product

from . import graph_base
from .clique_tree import CliqueTree

class GraphicalModel(graph_base.GraphBase):
    """Represents a graphical model."""
    def __init__(self, clique_potentials=None, sepset_potentials=None):
        """
        Create a new graphical model. clique_potentials is a list of
        tables, one for each clique. sepset_potentials is a list of
        tables for each sepset.  

        Tables are stored as dictionaries from assignment -> log
        probability.

        It is assumed that the graphical model is acyclic.
        """
        graph_base.GraphBase.__init__(self)

        if clique_potentials is None:
            clique_potentials = []

        if sepset_potentials is None:
            sepset_potentials = []

        self.sepset_potentials = sepset_potentials
        self.cl
