import weakref

import numpy as np

from .. import context
from .. import util


class Node(object):
    """
    Base class for all nodes.

    Parameters
    ----------
    inputs : list of Node objects
        Inputs to the node.
    outputs : list of Node objects
        Outputs from the node.
    name : str
        Name of the node.

    Attributes
    ----------
    inputs : list of Node objects
        Inputs to the node.
    outputs : list of Node objects
        Outputs from the node.
    name : str
        Name of the node.
    """

    def __init__(self, inputs=None, outputs=None, name=None):
        self.inputs = [] if inputs is None else inputs
        self.outputs = [] if outputs is None else outputs
        self.name = name

    def __str__(self):
        return '%s(%s)' % (self.name, ', '.join(i.name for i in self.inputs))

    def __repr__(self):
        return '%s(%
