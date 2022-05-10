import gc, weakref, operator # for graph
from pyeda.util import bitvec

import networkx as nx

#===============================================================================
# Data structures
#===============================================================================
class State:
    def __init__(self, num, cube, xs=None, ns=None):
        assert((xs is None) and (ns is None)) or (len(xs) == len(ns))
        self.num = num
        self.cube = cube
        if xs is None:
            self.xs = []
            self.ns = []
        else:
            self.xs = xs
            self.ns = ns

    def copy(self):
        return State(self.num, self.cube, self.xs[:], self.ns[:])

    def __str__(self):
        return str(self.num) + ": " + str(self.cube) + " " + str(self.xs) + " " + str(self.ns)

    def __repr__(self):
        return "S({0}, {1})".format(self.num, self.cube
