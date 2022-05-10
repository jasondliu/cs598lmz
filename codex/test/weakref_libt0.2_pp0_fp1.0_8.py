import weakref

from . import _base
from . import _util

class _BaseObject(_base.Object):
    """
    Base class for all objects.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the object.
        """
        super(_BaseObject, self).__init__(*args, **kwargs)
        self._parent = None
        self._children = []

    def _get_parent(self):
        """
        Get the parent of this object.
        """
        return self._parent

    def _set_parent(self, parent):
        """
        Set the parent of this object.
        """
        if self._parent is not None:
            self._parent._children.remove(self)
        self._parent = parent
        if parent is not None:
            parent._children.append(self)

    parent = property(_get_parent, _set_parent)

    def _get_children(self):
        """
        Get the children of this object.
        """
        return self._children

