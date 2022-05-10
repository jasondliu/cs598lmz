import weakref

from . import lib
from .default_attributes import DefaultAttributes
from . import _prop
from . import _widget


class Container(DefaultAttributes, _widget.Widget):
    """
    Container widget.

    A container is an abstract widget which has only an empty implementation
    of the draw() method. All other methods are implemented.
    """

    def __init__(self, window, **kwargs):
        """
        Initialize a new Container widget.

        :Parameters:
            `window` : `Window`
                The window where the container will be placed.
        """
        _widget.Widget.__init__(self, window, **kwargs)
        self._children = []

    def draw(self):
        """Draw the container."""
        raise NotImplementedError()

    def _set_parent(self, parent):
        """
        Set the container parent.

        :Parameters:
            `parent` : `Container`
                The new container parent.
        """
        _widget.Widget._set_parent(self, parent)
