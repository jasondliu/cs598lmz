import gc, weakref

from . import _compat
from . import _util

#-------------------------------------------------------------------------------

class _Base(object):
    """
    Base class for all objects in the scene graph.
    """

    #---------------------------------------------------------------------------
    # Object construction and destruction
    #---------------------------------------------------------------------------

    def __init__(self, name=None):
        """
        Initialize the object.
        """
        self._name = name
        self._parent = None
        self._children = []
        self._weakref = None

    def __del__(self):
        """
        Finalize the object.
        """
        self._parent = None
        self._children = []
        self._weakref = None

    #---------------------------------------------------------------------------
    # Object properties
    #---------------------------------------------------------------------------

    @property
    def name(self):
        """
        The name of the object.
        """
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def parent(self):
        """
        The parent of this object in the scene graph
