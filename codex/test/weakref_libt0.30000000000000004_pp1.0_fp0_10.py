import weakref

from .base import Base
from . import constants
from . import utils

class Node(Base):
    """
    A node is a single point in the graph. It has a unique ID, a label, and a
    dictionary of properties.
    """
    def __init__(self, id, labels=None, properties=None, **kwargs):
        """
        Create a new node.

        :param id: The ID of the node.
        :param labels: An iterable of labels for the node.
        :param properties: A dictionary of properties for the node.
        """
        self.id = id
        self.labels = labels or []
        self.properties = properties or {}
        self.graph = kwargs.get("graph", None)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)

