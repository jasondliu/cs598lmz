import weakref

import pymel.core as pm

import mgear.core.transform as tra
import mgear.core.node as node

##########################################################
# NODE NETWORK
##########################################################


class NodeNetwork(object):
    """
    NodeNetwork class.

    This class contains the methods to create, manage and
    delete the nodes used by the components.

    """

    def __init__(self, parent, name="network"):
        """Initialize the node network.

        Args:
            parent (dagNode): The parent of the network.
            name (str): The name of the network.

        """

        self.parent = parent
        self.name = name
        self.nodes = {}
        self.connections = {}
        self.build()

    # =====================================================
    # ATTRIBUTES
    # =====================================================
    @property
    def parent(self):
        """dagNode: The parent of the network."""
        return self._parent

    @parent.setter
    def parent(self, parent):
        if not
