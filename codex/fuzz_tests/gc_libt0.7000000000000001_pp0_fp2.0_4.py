import gc, weakref
import traceback

from . import _

class Node(object):
    """Base class for nodes.
    """
    def __init__(self, parent, label):
        self._children = []
        self._parent = None
        self._label = label
        self._name = self._label.lower().replace(" ", "_")
        self._uuid = uuid.uuid4().hex
        self._state = {}
        self._state_dirty = False
        self._state_lock = threading.RLock()

        self.set_parent(parent)

    def get_parent(self):
        """Returns the parent node.
        """
        return self._parent

    def add_child(self, child):
        """Adds a child node.
        """
        self._children.append(child)
        child.set_parent(self)

    def get_children(self):
        """Returns the list of children nodes.
        """
        return self._children

    def get_label(self):
        """Returns the node label.
        """
        return self._
